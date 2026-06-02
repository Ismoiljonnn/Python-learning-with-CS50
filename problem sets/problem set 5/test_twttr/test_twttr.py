from twttr import shorten


def test_shorten():
  assert shorten("twitter") == "twttr"
  assert shorten("HELLO") == "HLL"
  assert shorten("apple") == "ppl"

def test_numbers():
  assert shorten("1234") == "1234"

def test_punctuation():
  assert shorten("!?.") == "!?."