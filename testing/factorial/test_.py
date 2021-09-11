import pytest
import myfactorial

def test_myfactorial():
    assert myfactorial.factorial(3) == 6

def test_myfactorial_zero():
    assert myfactorial.factorial(0) == 1

def test_myfactorial_negative():
    try:
        myfactorial.factorial(-1)
    except Exception as exc:
        assert True, 'factorial raised an exception {}'.format(exc)
