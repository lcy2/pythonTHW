from nose.tools import *
from CH16P18 import pat_matcher

def test_pattern():
    assert_true(pat_matcher.match("catcatgocatgo", "aabab"))
    assert_true(pat_matcher.match("catcatgocatgo", "ab"))