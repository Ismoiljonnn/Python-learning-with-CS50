students = [
  {"name": "Hermione", "house": "Gryffindor"},
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Ron", "house": "Gryffindor"},
  {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(s):
  return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)