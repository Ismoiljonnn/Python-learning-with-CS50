try:
  x = int(input("What's x? "))
except ValueError:
  print("x is not and integer")
else:
  print(f"x is {x}") 