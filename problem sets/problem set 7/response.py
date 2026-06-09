import re
import sys


def main():
  print(validate(input("What's your email address? ")))


def validate(s):
  if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$", s):
    return "Valid"
  return "Invalid"


if __name__ == "__main__":
  main()