import pytest
from extract_position import extract_position

def test_extract_position_1():
    line = '|error| numerical calculations could not converge.'
    assert extract_position(line) is None

def test_extract_position_2():
    line = '|update| the positron location in the particle accelerator is x:21.432'
    assert extract_position(line) == '21.432'

def test_extract_position_3():
    line = '|debug| the positron location in the particle accelerator is x:21.432'
    assert extract_position(line) is None
