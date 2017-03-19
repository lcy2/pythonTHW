from nose.tools import *
from C16P02.word_counter import word_counter
import os

# according to https://wordcounter.net/
# roger 24 (7%)
# arm 15 (5%)
# mate 7 (2%)
# roger's 5 (2%)
# right 5 (2%)
# asked 5 (2%)
# about 5 (2%)
# left 4 (1%)
# side 4 (1%)
# back 4 (1%)


def word_counter_test():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


    with open(os.path.join(__location__, "test_paragraph.txt")) as f:
        
        wc = word_counter(f)
        assert_equal(wc.get_word_count("roger"), 24)
        assert_equal(wc.get_word_count("arm"), 15)

if __name__ == "__main__":
    word_counter_test()