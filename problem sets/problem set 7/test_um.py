import pytest
from um import count

def test_um_basic():
    assert count("um") == 1
    assert count("um, um, um") == 3

def test_um_case_insensitive():
    assert count("Um, UM, um") == 3

def test_um_word_boundaries():
    assert count("humour") == 0
    assert count("yummy") == 0
    assert count("um?") == 1

def test_um_surrounded_by_space():
    assert count("hello um world") == 1