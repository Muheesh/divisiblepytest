import divisible
import pytest
@pytest.fixture
def input():
    x = 16
    return x

def test_div8(input):
    res = divisible.div_8(input)
    assert res == True

def test_div9(input):
    result = divisible.div_9(input)
    assert  result == True

def test_div10(input):
    result = divisible.div_10(input)
    assert result == True
