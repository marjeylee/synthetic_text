import hashlib
import os
import datetime
import shutil

from container_annotation.copy_file import get_all_file_from_dir


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return str(myhash.hexdigest())


if __name__ == '__main__':

    dir_path = 'D:/BaiduNetdiskDownload/daokou_all/'
    des_path = 'D:/image/all_daokou_md5/'
    paths = get_all_file_from_dir(dir_path)
    length = len(paths)
    index = 0
    for path in reversed(paths):
        # if index < 50000:
        #     continue
        index = index + 1
        if '.jpg' in path:
            try:
                if index % 1000 == 0:
                    print(str(index) + '/' + str(length))
                name = GetFileMd5(path) + '.jpg'
                shutil.copy(path, des_path + name)
            except Exception as e:
                print(e)
