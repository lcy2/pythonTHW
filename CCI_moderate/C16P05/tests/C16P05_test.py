from nose.tools import *
from C16P05 import finder

def fac_zero_test():
    assert_equal(finder.find(100), 24)