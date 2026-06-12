import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    birth_date_str = input("Date of Birth: ")
    birth_date = validate_date(birth_date_str)
    
    minutes = calculate_minutes(birth_date, date.today())
    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")

def validate_date(date_str):
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        sys.exit("Invalid date")

def calculate_minutes(birth, today):
    delta = today - birth
    return delta.days * 24 * 60

if __name__ == "__main__":
    main()