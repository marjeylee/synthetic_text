# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cluster_text_area
   Description :
   Author :       'li'
   date：          2018/8/30
-------------------------------------------------
   Change Activity:
                   2018/8/30:
-------------------------------------------------
"""
import time
from collections import defaultdict
from collections import Counter

from dlmodel.single_box_recognize import model_log
from dlmodel.single_box_recognize.check.check_11_number import check_11_number
from dlmodel.single_box_recognize.process_images.result import result
import numpy as np

from dlmodel.single_box_recognize.utility.edit_distance import get_edit_distance

__author__ = 'li'

log = model_log


def add_center_point(img_des):
    """
    add center point
    :param img_des:
    :return:
    """
    for des in img_des:
        x, y = int((des[0]['x0'] + des[0]['x2']) / 2), int((des[0]['y0'] + des[0]['y2']) / 2)
        des.append([x, y])
    return img_des


def calu_distance(co1, co2):
    d_x = co1[0] - co2[0]
    d_y = co1[1] - co2[1]
    return np.sqrt((np.square(d_x) + np.square(d_y)))


def decode_cluster(cluster, img_des):
    """
    return coordinate
    :param cluster:
    :param img_des:
    :return:
    """
    return_cluster = []
    for index in cluster:
        cl = [img_des[index]]
        vs = cluster[index]
        if len(vs) < 1:
            continue
        for v in vs:
            cl.append(img_des[v])
        return_cluster.append(cl)
    return return_cluster


def cluster_text_area(img_des):
    """
    cluster one image`s text area
    :param img_des:
    :return:
    """
    if len(img_des) < 1:
        return None
    centers = []
    cluster = {}
    img_des = add_center_point(img_des)
    for index in range(len(img_des)):  # get center text area :six num digit
        text = img_des[index][1]
        if text.isdigit() and len(text) > 2:
            centers.append(index)
            cluster[index] = []
    for i in range(len(img_des)):  # cluster
        if i in centers:
            continue
        coor = img_des[i][2]
        cp = None
        if len(centers) == 0:
            continue
        for c in centers:  # loop center point get the nearest
            if cp is None:
                cp = c
            elif calu_distance(img_des[cp][2], coor) > calu_distance(img_des[c][2], coor):
                cp = c
        cluster[cp].append(i)
    return decode_cluster(cluster, img_des)


def get_images_cluster(result):
    cluster_results = []
    for img_name in result:
        img_des = result[img_name]
        cluster_result = cluster_text_area(img_des)
        content = {'img_name': img_name, 'cluster_result': cluster_result}
        cluster_results.append(content)
    return cluster_results


def get_box_holder_num(c, box_num):
    """
    get box holder num
    :param c:
    :return:
    """
    tmp_holder_num = None
    for text_area in c:
        num = text_area[1]  # 1 means box num
        if len(num) < 2:
            continue
        if 'QWERTYUIOPLKJHGFDSAZXCVBNM'.find(num[0]) >= 0 and 'QWERTYUIOPLKJHGFDSAZXCVBNM'.find(num[1]) >= 0:
            if tmp_holder_num is None:
                tmp_holder_num = text_area
            # find the nearest region
            elif calu_distance(tmp_holder_num[2], box_num[2]) > calu_distance(text_area[2], box_num[2]):
                tmp_holder_num = text_area
    return tmp_holder_num


def get_box_num(c):
    """
    get box num ,box num is center of cluster,every cluster has one box num
    :param c:
    :return:
    """
    if len(c) == 0:
        return None
    for text_area in c:
        num = text_area[1]  # 1 means box num
        if num.isdigit() and len(num) > 2:
            return text_area
    return None


def get_box_type(c, box_num):
    """
    get nearest box type
    :param c:
    :param box_num:
    :return:
    """
    tmp_box_type = None
    for text_area in c:
        num = text_area[1]  # 1 means box num
        if len(num) < 3:
            continue
        if '1234567890'.find(num[0]) >= 0 and '1234567890'.find(num[1]) >= 0 \
                and 'QWERTYUIOPLKJHGFDSAZXCVBNM'.find(num[2]) >= 0:
            if tmp_box_type is None:
                tmp_box_type = text_area
            # find the nearest region
            elif calu_distance(tmp_box_type[2], box_num[2]) > calu_distance(text_area[2], box_num[2]):
                tmp_box_type = text_area
    return tmp_box_type


def get_validation_num(c, box_num):
    """
        get nearest box type
        :param c:
        :param box_num:
        :return:
        """
    tmp_validation_num = None
    for text_area in c:
        num = text_area[1].replace('#', '')  # 1 means box num
        if len(num) != 1:
            continue
        if '1234567890'.find(num[0]) >= 0:
            if tmp_validation_num is None:
                tmp_validation_num = text_area
            # find the nearest region
            elif calu_distance(tmp_validation_num[2], box_num[2]) > calu_distance(text_area[2], box_num[2]):
                tmp_validation_num = text_area
    return tmp_validation_num


def get_prediction_results(results):
    """
    every image could contain one or more cluster,so this function create a set of
    container result for every cluster.if specific content is not include,make it empty,\
    otherwise,drop out text area farther away/
    :param results:
    :return:
    """
    if len(results) == 0:
        return None
    prediction_results = []
    for r in results:  # for loop every image
        cluster_result = r['cluster_result']
        if cluster_result is None:
            continue
        if len(cluster_result) == 0:
            r['prediction_results'] = []
            continue
        prediction = {'img_name': r['img_name']}
        content_prediction = []
        for c in cluster_result:  # for loop every cluster
            box_num = get_box_num(c)
            if box_num is None:
                continue
            box_holder_num = get_box_holder_num(c, box_num)
            box_type = get_box_type(c, box_num)
            validation_num = get_validation_num(c, box_num)
            cluster_prediction = {'box_num': box_num, 'box_holder_num': box_holder_num, 'box_type': box_type,
                                  'validation_num': validation_num}
            content_prediction.append(cluster_prediction)
        prediction['cluster_prediction'] = content_prediction
        prediction_results.append(prediction)
    return prediction_results


def parse_prediction_result(prediction):
    """
    parse result
    :param prediction:
    :return:
    """
    sum_result = []
    for img in prediction:
        img_result = {'img_name': img['img_name']}
        cluster_prediction = img['cluster_prediction']
        img_result['recognition_result'] = []
        if len(cluster_prediction) == 0:
            sum_result.append(img_result)
            continue
        for c in cluster_prediction:
            box_num = None
            box_holder_num = None
            box_type = None
            validation_num = None
            if c['box_num'] is not None:
                box_num = c['box_num'][1]
            if c['box_holder_num'] is not None:
                box_holder_num = c['box_holder_num'][1]
            if c['box_type'] is not None:
                box_type = c['box_type'][1]
            if c['validation_num'] is not None:
                validation_num = c['validation_num'][1]
            re = {'box_num': box_num, 'box_holder_num': box_holder_num, 'box_type': box_type,
                  'validation_num': validation_num}
            img_result['recognition_result'].append(re)
        sum_result.append(img_result)
    return sum_result


def is_two_box(stat):
    """
        is two box
        :param stat:
        :return:
        """
    if len(stat) < 2:
        return False
    if len(str(stat[1][0])) != 6:
        return False
    if stat[1][1] == 1:
        return False
    if stat[0][1] / stat[1][1] < 2:
        return True
    return False


def get_highest_frequency_element(lst):
    """
    :param lst:
    :return:
    """
    if lst is None or len(lst) == 0:
        return None
    com = Counter(lst).most_common(1)[0]
    if com[0] is None:
        try:
            com = Counter(lst).most_common(2)[1]
        except Exception as e:
            print(e)
        finally:
            return com
    else:
        return com


def filter_box_holder_num(lst):
    if len(lst) == 0:
        return None
    new_lst = []
    for item in lst:
        if len(item) == 4:
            new_lst.append(item)
    if len(new_lst) == 0:
        return lst
    return new_lst


def get_two_box_num(merge_result, stat):
    """
    get two boxes num with maximum probability
    :param merge_result:
    :param stat:
    :return:
    """
    recommended_results = []
    for i in range(2):
        tmp_box_num = stat[i][0]
        tmp_dict = merge_result[tmp_box_num]
        tmp_dict['box_holder_num'] = filter_box_holder_num(tmp_dict['box_holder_num'])
        box_holder_num = get_highest_frequency_element(tmp_dict['box_holder_num'])
        box_type = get_highest_frequency_element(tmp_dict['box_type'])
        validation_num = get_highest_frequency_element(tmp_dict['validation_num'])
        if box_type is None:
            box_type = ['unrecognize']
        if validation_num is None:
            validation_num = [-1]
        if box_holder_num is None:
            box_holder_num = ['unrecognize']
        res = {'box_num': tmp_box_num, 'box_holder_num': box_holder_num[0], 'box_type': box_type[0],
               'validation_num': validation_num[0]}
        recommended_results.append(res)
    return recommended_results


def get_merge_result(prediction_result):
    """
    merge result
    :param prediction_result:
    :return:
    """
    merge_result = {}
    for img in prediction_result:
        recognition_result = img['recognition_result']
        for c in recognition_result:
            box_num = c['box_num']
            if box_num in merge_result.keys():
                tmp_dict = merge_result[box_num]
                if c['box_holder_num'] is not None and len(c['box_holder_num']) == 4:
                    tmp_dict['box_holder_num'].append(c['box_holder_num'])
                if c['box_type'] is not None:
                    tmp_dict['box_type'].append(c['box_type'])
                if c['validation_num'] is not None:
                    tmp_dict['validation_num'].append(c['validation_num'].replace('#', ''))
                merge_result[box_num] = tmp_dict
            else:
                tmp_dict = {'box_holder_num': [], 'box_type': [],
                            'validation_num': []}
                if c['box_holder_num'] is not None and len(c['box_holder_num']) == 4:
                    tmp_dict['box_holder_num'].append(c['box_holder_num'])
                if c['box_type'] is not None:
                    tmp_dict['box_type'].append(c['box_type'])
                if c['validation_num'] is not None:
                    tmp_dict['validation_num'].append(c['validation_num'].replace('#', ''))
                merge_result[box_num] = tmp_dict
    return merge_result


def one_box_get_highest_frequency_element(merge_result, key_type, tmp_box_num=None):
    nums = merge_result.keys()
    statistic_list = []
    for num in nums:
        if tmp_box_num is not None:
            if tmp_box_num == num:
                tmp_list = merge_result[num][key_type]
                statistic_list = statistic_list + tmp_list
        else:
            tmp_list = merge_result[num][key_type]
            statistic_list = statistic_list + tmp_list
    if len(statistic_list) == 0:
        return None
    sorted_key = get_highest_frequency_element(statistic_list)[0]
    return sorted_key


def get_right_box_num(validate_result):
    """
    get highest frequency num and result
    :param validate_result:
    :return:
    """
    statistic_list = []
    for ele in validate_result:
        right_box = ele['right_code']
        statistic_list.append(right_box)
    sorted_key = get_highest_frequency_element(statistic_list)[0]
    for ele in validate_result:
        right_box = ele['right_code']
        if right_box == sorted_key:
            return ele['right_owner'], ele['right_code'], ele['verification']
    return None


def get_one_box_num(merge_result, stat, validate_result):
    """
    :param validate_result:
    :param merge_result:
    :param stat:
    :return:
    """
    if len(stat) == 0:
        return []
    if stat[0][1] == 1 and len(validate_result) > 0:
        box_holder_num, tmp_box_num, validation_num = get_right_box_num(validate_result)
    else:
        tmp_box_num = stat[0][0]
        box_holder_num = one_box_get_highest_frequency_element(merge_result, 'box_holder_num')
        validation_num = one_box_get_highest_frequency_element(merge_result, 'validation_num', tmp_box_num)
    box_type = one_box_get_highest_frequency_element(merge_result, 'box_type')

    res = {'box_num': tmp_box_num, 'box_holder_num': box_holder_num, 'box_type': box_type,
           'validation_num': validation_num}
    return [res]


def filter_validate_num(merge_result):
    """
    remove # in validation num
    :param merge_result:
    :return:
    """
    for num in merge_result.keys():
        if 'validation_num' in merge_result[num]:
            validation_list = merge_result[num]['validation_num']
            tmp_list = []
            for ele in validation_list:
                if ele is None:
                    continue
                if len(ele) == 2 and ele[0] == '#':
                    ele = ele.replace('#', '')
                    tmp_list.append(ele)
                else:
                    tmp_list.append(ele)
            merge_result[num]['validation_num'] = tmp_list


def statistic_box_num(box_num_statistic):
    """
    statistic box
    :param box_num_statistic:
    :return:
    """
    sort_list = sorted(box_num_statistic.items(), key=lambda e: e[1], reverse=True)
    for item in sort_list:
        num = item[0]
        if len(num) != 6:
            sort_list.remove(item)
    return sort_list


def validate_single_cluster(cluster_result):
    box_holder_num = cluster_result['box_holder_num']
    box_num = cluster_result['box_num']
    validation_num = cluster_result['validation_num']
    if not validation_num.isdigit():
        if validation_num.find('#') >= 0:
            validation_num = validation_num.replace('#', '')
    validation_num = int(validation_num)
    check_result = check_11_number(
        {"carton_owner": box_holder_num, "carton_code": str(box_num), "verification": validation_num,
         "carton_type_code": "22G1"})
    if check_result[0][0] == 0 and check_result[1] == 0 and check_result[2] == 0:
        return {"right_owner": box_holder_num, "right_code": str(box_num), "verification": validation_num}
    return None


def pre_check_every_cluster(prediction_result):
    """
    check every cluster, return right check result ,
    including container holder num ,box num, validate num.
    :param prediction_result:
    :return:
    """
    if prediction_result is None or len(prediction_result) == 0:
        return None
    check_result = []
    for image_result in prediction_result:
        if 'recognition_result' in image_result.keys():
            recognition_result = image_result['recognition_result']
            if recognition_result is None or len(recognition_result) == 0:
                continue
            for cluster_result in recognition_result:
                if cluster_result['box_num'] is None \
                        or cluster_result['box_holder_num'] is None \
                        or cluster_result['validation_num'] is None \
                        or len(cluster_result['box_num']) != 6 \
                        or len(cluster_result['box_holder_num']) != 4:
                    continue
                validate_result = validate_single_cluster(cluster_result)
                if validate_result is not None:
                    check_result.append(validate_result)
    return check_result


def statistics_result(prediction_result):
    """
    统计结果
    :param prediction_result:
    :return:
    """
    validate_result = pre_check_every_cluster(prediction_result)
    box_num_statistic = defaultdict(int)
    for img in prediction_result:
        recognition_result = img['recognition_result']
        for c in recognition_result:
            box_num = c['box_num']
            box_num_statistic[box_num] = box_num_statistic[box_num] + 1
    stat = statistic_box_num(box_num_statistic)
    is_two = is_two_box(stat)
    merge_result = get_merge_result(prediction_result)
    filter_validate_num(merge_result)
    if len(merge_result.keys()) == 0:
        return None
    if is_two:
        two_box_num = get_two_box_num(merge_result, stat)
        return two_box_num
    if not is_two:
        one_box_num = get_one_box_num(merge_result, stat, validate_result)
        return one_box_num


def check_box_num(statistics_results):
    """
    校验结果
    :param statistics_results:
    :return:
    """
    if statistics_results is None or len(statistics_results) == 0:
        return None
    check_results = []
    for s in statistics_results:
        if s['box_holder_num'] is None:
            s['box_holder_num'] = 'undefined'
        if s['box_num'] is None:
            s['box_num'] = 0
        if s['validation_num'] is None:
            s['validation_num'] = -1
        if s['box_type'] is None:
            s['box_type'] = 'undefined'
        s['validation_num'] = str(s['validation_num']).replace('#', '')
        transform_obj = {"carton_owner": s['box_holder_num'], "carton_code": str(s['box_num']),
                         "verification": int(s['validation_num']),
                         "carton_type_code": s['box_type']}
        result = check_11_number(transform_obj)
        check_result = {'box_num': transform_obj, 'check_result': result}
        check_results.append(check_result)
    return check_results


def filter_check_result(check_results):
    """
    filter check result
    :param check_results:
    :return:
    """
    if check_results is None:
        return None
    if len(check_results) == 1:
        return check_results
    if len(check_results) == 2:
        check_result1 = check_results[0]['check_result']
        check_result2 = check_results[1]['check_result']
        if (check_result1[0][0] == check_result1[1] == check_result1[2] == check_result1[3][0] == 0) and (
                check_result2[0][0] == check_result2[1] == check_result2[2] == check_result2[3][0] == 0):
            """all right"""
            return check_results
        if not (check_result1[0][0] == check_result1[1] == check_result1[2] == check_result1[3][0] == 0) and (
                check_result2[0][0] == check_result2[1] == check_result2[2] == check_result2[3][0] == 0):
            """one wrong,one right"""
            box_num1 = check_results[0]['box_num']  # wrong
            box_num2 = check_results[1]['box_num']  # right
            if (get_edit_distance(box_num1['carton_owner'], box_num2['carton_owner']) < 2) and (
                    get_edit_distance(box_num1['carton_code'], box_num2['carton_code']) < 2):  # similar
                return [check_results[1]]
        if (check_result1[0][0] == check_result1[1] == check_result1[2] == check_result1[3][0] == 0) and not (
                check_result2[0][0] == check_result2[1] == check_result2[2] == check_result2[3][0] == 0):
            """one wrong,one right"""
            box_num1 = check_results[0]['box_num']  # right
            box_num2 = check_results[1]['box_num']  # wrong
            if (get_edit_distance(box_num1['carton_owner'], box_num2['carton_owner']) < 2) and (
                    get_edit_distance(box_num1['carton_code'], box_num2['carton_code']) < 2):  # similar
                return [check_results[0]]
    return check_results


def cluster_and_check_result(result):
    """
    cluster coordination and check some value
    :param result:
    :return:
    """
    start_time = time.time()
    results = get_images_cluster(result)  # get every image`s text area cluster
    prediction = get_prediction_results(results)
    if len(prediction) == 0:
        return None
    prediction_result = parse_prediction_result(prediction)
    statistics_results = statistics_result(prediction_result)
    end_time = time.time()
    duration = end_time - start_time
    log.info('cluster result,use ' + str(duration) + ' second')
    start_time = time.time()
    """check start"""
    check_result = check_box_num(statistics_results)
    end_time = time.time()
    duration = end_time - start_time
    log.info('check result,use ' + str(duration) + ' second')
    check_result = filter_check_result(check_result)
    return check_result


def main():
    results = get_images_cluster(result)
    prediction = get_prediction_results(results)
    prediction_result = parse_prediction_result(prediction)
    statistics_results = statistics_result(prediction_result)
    check_result = check_box_num(statistics_results)
    pass


if __name__ == '__main__':
    main()
