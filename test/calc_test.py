import pytest
from calc.calc import Calc

calc = Calc()

def test_add():
    assert calc.add(1, 2) == 3

def test_subtract():
    assert calc.subtract(5, 2) == 3

def test_multiply():
    assert calc.multiply(3, 4) == 12

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(10, 0)

#selhat
def test_failed_add():
    assert calc.add(1, 2) == 4

def test_failed_subtract():
    assert calc.subtract(5, 2) == 2
