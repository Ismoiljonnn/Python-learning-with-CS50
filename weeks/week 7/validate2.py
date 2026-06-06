import re

email = input("What's your email? ").strip().lower()

if re.search(r"^\w.+@[a-zA-Z0-9_]+\.edu$", email):
  print("Valid")
else:
  print("Invalid")