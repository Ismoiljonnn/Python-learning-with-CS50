from fuel import convert, gauge
import pytest

def test_convert():
  assert convert("1/4") == 25
  assert convert("1/100") == 1
  assert convert("99/100") == 99

def test_gauge():
  assert gauge(1) == "E"
  assert gauge(99) == "F"
  assert gauge(50) == "50%"

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/4")

def test_convert_errors():
  with pytest.raises(ValueError):
    convert("cat/dog")
  with pytest.raises(ZeroDivisionError):
    convert("1/0")