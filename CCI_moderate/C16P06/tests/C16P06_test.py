from nose.tools import *
from C16P06 import solution

def dif_test():
    ans =solution.smallest_dif([1,3,15,11,2], [23, 127, 235, 19, 8])
    assert_equal(ans, 3)