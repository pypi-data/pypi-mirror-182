"""Some useful code for math.
@author: Rui Zhu
@creation time: 2022-12-22
"""
import numpy as np

def crack(integer):
    """
    将一个整数(integer)分成两个相近整数的乘积(a*b)
    """
    a = int(np.sqrt(integer))
    b = integer / a
    while int(b) != b:
        a += 1
        b = integer / a
    return int(a), int(b)