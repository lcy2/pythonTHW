from nose.tools import *
from C16P01 import C16P01
import random
import sys

def swap_test():
    a = random.randint(-sys.maxint - 1, sys.maxint)
    b = random.randint(-sys.maxint - 1, sys.maxint)
    
    new_a, new_b = C16P01.swap_nums(a, b)
    
    assert_equal(new_a, b)
    assert_equal(new_b, a)