import divisible
import pytest
def test_div8():
    a = 16
    res = divisible.div_8(a)
    assert res == True
def test_div9():
    a = 54
    result = divisible.div_9(a)
    assert  result == True
def test_div10():
    a = 1000
    result = divisible.div_10(a)
    assert result == True
