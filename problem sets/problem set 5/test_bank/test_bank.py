from bank import value

def test_value():
  assert value("HELLO") == 0
  assert value("hello") == 0
  assert value("Hello") == 0

  assert value("How are you?") == 20
  assert value("h") == 20

  assert value("What's up") == 100
  assert value() == 100
  assert value("goole") == 100

  assert value("  hello  ") == 0