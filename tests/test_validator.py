# Tests for validator module
from src.validator import is_positive
from src.utils import add

def test_add():
    assert add(2, 3) == 5

def test_is_positive():
    assert is_positive(-1) is False
