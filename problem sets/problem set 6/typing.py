import sys

def main():
  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

  if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

  try:
    with open(sys.argv[1], "r") as file:
      lines = file.readlines()
  except FileNotFoundError:
    sys.exit("File does not exist")
  
  count = 0
  for line in lines:
    stripped = line.lstrip()
    if stripped and not stripped.startswith("#"):
      count += 1

  print(count)


if __name__ == "__main__":
  main()