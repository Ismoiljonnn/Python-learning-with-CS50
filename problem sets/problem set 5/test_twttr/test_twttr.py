from twttr import shorten


def test_shorten():
  assert shorten("twitter") == "twttr"
  assert shorten("HELLO") == "HLL"
  assert shorten("apple") == "ppl"