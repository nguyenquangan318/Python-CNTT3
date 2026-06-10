import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    
def test_text_input():
    assert add('a', 'b') == None