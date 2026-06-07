import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
  last = matches.group(1)
  first = matches.group(2)
print(f"hello, {name}")