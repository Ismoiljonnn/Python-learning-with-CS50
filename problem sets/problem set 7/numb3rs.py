import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))
        
def validate(ip):
    octet = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
    pattern = rf"^{octet}\.{octet}\.{octet}\.{octet}$"
    
    if re.search(pattern, ip):
        return True
    return False

if __name__ == "__main__":
    main()