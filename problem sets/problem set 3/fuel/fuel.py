def main():
  foiz = get_fuel_persentage()
  if foiz <= 1:
    print("E")
  elif foiz >= 99:
    print("F")
  else:
    print(f"{foiz}%")


def get_fuel_persentage():
  while True:
    fraction = input("Fraction: ")
    try:
      x_str, y_str = fraction.split("/")
      x = int(x_str)
      y = int(y_str)

      if y == 0:
        raise ZeroDivisionError
      
      if x < 0 or x > y:
        continue

      percentage = round((x / y) * 100)
      return percentage

    except (ValueError, ZeroDivisionError):
      pass

main()