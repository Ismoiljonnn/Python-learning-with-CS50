from numb3rs import validate

def test_format():
  assert validate("1.2.3.4") == True
  assert validate("127.0.0.1") == True
  assert validate("255.255.255.255") == True
  assert validate("0.0.0.0") == True

def test_out_of_range():
  assert validate("256.1.1.1") == False
  assert validate("1.256.1.1") == False
  assert validate("1.1.256.1") == False
  assert validate("1.1.1.256") == False
  assert validate("300.300.300.300") == False

def test_wrong_format():
  assert validate("1.2.3") == False
  assert validate("1.2.3.4.5") == False
  assert validate("a.b.c.d") == False
  assert validate("1.2.3.a") == False
  assert validate("cat") == False