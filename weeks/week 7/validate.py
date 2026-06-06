email = input("What's your email? ").strip()

username, domain = email.split("@")

if username:
  print("Valid")
else:
  print("Invalid")