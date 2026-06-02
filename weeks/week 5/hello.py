def main():
  name = input("What's your name? ")
  output = hello(name)
  print(output)


def hello(to="world"):
  return f"hello", {to}

if __name__ == "__main__":
  main()