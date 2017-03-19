from nose.tools import *
from C16P08 import maxxer
import sys
import random

def max_test():
    a = random.randint(-sys.maxint - 1, sys.maxint)
    b = random.randint(-sys.maxint - 1, sys.maxint)
    assert_equal(maxxer.get_max(a, b), max(a,b))
    
    