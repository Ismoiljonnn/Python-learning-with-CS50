import re

url = input("URL: ").strip()

username = re.sub(f"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")