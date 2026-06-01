from calculator import square


def main():
  test_square()


def test_square():
  assert square(2) == 4
  assert square(2) == 9


if __name__ == "__main__":
  main()