import numpy as np

from config import CHAR_MAX_NUM_PER_IMAGE

for i in range(100):
    num = np.random.randint(0, CHAR_MAX_NUM_PER_IMAGE + 1, dtype=int)
    print(num)
