def main():
  fraction = input("Fraction: ")
  percentage = convert(fraction)
  print(gauge(percentage))


def convert(fraction):
  while True:
    try:
      x, y = fraction.split("/")
      x, y = int(x), int(y)
      if y == 0:
        raise ZeroDivisionError
      if x > y:
        fraction = input("Fraction: ")
        continue
      return round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
      fraction = input("Fraction: ")
      continue


def gauge(percentage):
  if percentage <= 1:
    return "E"
  elif percentage >= 99:
    return "F"
  else:
    return f"{percentage}%"

if __name__ == "__main__":
  main()