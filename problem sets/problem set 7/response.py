import validators

def main():
    email = input("What's your email address? ")
    print(validate(email))

def validate(s):
    if validators.email(s):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()