def meow(n: int) -> str:
  """
  Meow n times.

  :param n: Nubmer of times to meow
  :type n: int
  :raise TypeError: If n is not an int
  :return: A string of n meows, one per line
  :rtype: str
  """
  return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")