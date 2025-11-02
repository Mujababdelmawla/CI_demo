from app import add, divide, multiplication,subtraction
import pytest

def test_add():
    assert add(2,3) == 5
    
def test_divide():
    assert divide(6,3) == 2
    
def test_multiplication():
    assert multiplication(10,2) ==20

def test_subtraction():
    assert subtraction(300,250) ==50

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

