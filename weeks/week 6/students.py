with open ("students.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    print(f"{name[0]} is in {house[1]}")