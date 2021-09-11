import pytest
import capitalize

def test_capital_case():
    assert capitalize.capital_case('test') == 'Test'

def test_capital_case_number():
    try:
        capitalize.capital_case('12')
    except Exception as exc:
        assert True, 'Capiral case raised an exception {}'.format(exc)

