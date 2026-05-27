students = [
  {"name": "Hermione", "house": "griffindor", "patronus": "Otter"},
  {"name": "Harry", "house": "griffindor", "patronus": "Stag"},
  {"name": "Ron", "house": "griffindor", "patronus": "Jack Russell terrier"},
  {"name": "Draco", "house": "slytherin", "patronus": None}
]

for student in students:
  print(student["name"], student["house"], student["patronus"], sep=", ")