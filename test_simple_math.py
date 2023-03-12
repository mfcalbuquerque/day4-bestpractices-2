import simple_math
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1,1,2),
    (1,2,3),
    (1,3,5)
    ])
def test_simple_math(a, b, expected):
    assert simple_math.simple_add(a,b) == expected
##
##
##def test_simple_math2():
##    assert simple_math.simple_div(10,2) == 4, "This operation is wrong"
