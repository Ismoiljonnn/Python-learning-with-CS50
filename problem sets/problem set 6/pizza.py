import sys
import csv
from tabulate import tabulate


def main():
  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

  filename = sys.argv[1]

  if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

  try:
    with open(filename, "r") as file:
      reader = csv.DictReader(file)
      table = list(reader)

      print(tabulate(table, headers="keys", tablefmt="grid"))

  except FileNotFoundError:
    sys.exit("File does not exist")


if __name__ == "__main__":
  main()
