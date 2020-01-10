import pytest

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

def sum(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2

@pytest.mark.parametrize('num1, num2, expected',[(3,5,8),              (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)])
def test_sum(num1, num2, expected):
        assert sum(num1, num2) == expected

@pytest.fixture
def get_sum_test_data():
        return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]


def test_sum2(get_sum_test_data):
        for data in get_sum_test_data:
                num1 = data[0]
                num2 = data[1]
                expected = data[2]
                assert sum(num1, num2) == expected