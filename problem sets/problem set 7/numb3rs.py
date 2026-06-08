import re
import sys

def main():
  print(validate(input("IPv4 Adress: ")))
        
def validate(ip):
  pattern = r"^([0-9][1-9][0-9]1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))$"


  if re.search(pattern, ip):
    return True
  else:
    return False


if __name__ == "__main__":
  main()