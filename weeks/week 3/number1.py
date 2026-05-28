try:
  x = int(input("What's x? "))
except ValueError:
  print("x is not and integer")

print(f"x is {x}")