students = []

with open("students.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    student = {}
    student = {"name": name, "house": house}
    students.append(student)


for student in students:
  print(f"{student['name']} is in {students['house']}")