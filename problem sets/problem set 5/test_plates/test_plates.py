from plates import is_valid

def test_length():
  assert is_valid("CS") == True
  assert is_valid("C") == False
  assert is_valid("CSCSCS") == True
  assert is_valid("CSCSCSC") == False

def test_alphabetical():
  assert is_valid("AA") == True
  assert is_valid("12") == False
  assert is_valid("A1") == False

def test_alphanumeric():
  assert is_valid("AA50") == True
  assert is_valid("AA.50") == False
  assert is_valid("AA 50") == False

def test_numbers():
  assert is_valid("AA12A") == False
  assert is_valid("AA05") == False