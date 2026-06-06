import re

email = input("What's your email? ").strip()

if re.search(r"^\w.+@[a-zA-Z0-9_]+\.edu$", re.IGNORECASE):
  print("Valid")
else:
  print("Invalid")