"""
JarvisCLI - A simple terminal-based personal assistant.

Final Project for CS50's Introduction to Programming with Python (CS50P).

Features:
- Add and view personal notes (saved to notes.txt)
- Check current weather for any city (via wttr.in, no API key needed)
- Check the strength of a password

Author: Ismoiljon
"""

import os
import re
import sys
import random
import requests
from datetime import datetime

NOTES_FILE = "notes.txt"


def clear_screen():
    """Clear the terminal screen (works on both Windows and Unix)."""
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    """Print the main menu."""
    print("\n" + "=" * 30)
    print("         JarvisCLI")
    print("=" * 30)
    print("1. Add a note")
    print("2. View notes")
    print("3. Check weather")
    print("4. Check password strength")
    print("5. Show current time")
    print("6. Show current date")
    print("7. Flip a coin")
    print("8. Roll a dice")
    print("9. Count words in a text")
    print("10. Convert Celsius to Fahrenheit")
    print("11. Calculate BMI")
    print("12. Exit")
    print("-" * 30)


def pause():
    """Wait for the user to press Enter before returning to the menu."""
    input("\nPress Enter to return to the menu...")


def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Choose an option (1-12): ").strip()

        if choice == "1":
            note = input("Enter your note: ").strip()
            print("\n" + add_note(note))
            pause()
        elif choice == "2":
            notes = get_notes()
            print()
            if not notes:
                print("You have no notes yet.")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note}")
            pause()
        elif choice == "3":
            city = input("Enter city name: ").strip()
            print("\n" + get_weather(city))
            pause()
        elif choice == "4":
            password = input("Enter password to check: ").strip()
            print(f"\nPassword strength: {password_strength(password)}")
            pause()
        elif choice == "5":
            print(f"\nCurrent time: {get_time()}")
            pause()
        elif choice == "6":
            print(f"\nToday's date: {get_date()}")
            pause()
        elif choice == "7":
            print(f"\nResult: {flip_coin()}")
            pause()
        elif choice == "8":
            sides = input("Number of sides (default 6): ").strip()
            sides = int(sides) if sides else 6
            print(f"\nYou rolled: {roll_dice(sides)}")
            pause()
        elif choice == "9":
            text = input("Enter your text: ").strip()
            print(f"\nWord count: {count_words(text)}")
            pause()
        elif choice == "10":
            celsius = input("Enter temperature in Celsius: ").strip()
            print(f"\n{celsius}°C = {celsius_to_fahrenheit(float(celsius))}°F")
            pause()
        elif choice == "11":
            weight = float(input("Enter weight in kg: ").strip())
            height = float(input("Enter height in cm: ").strip())
            print(f"\nYour BMI: {calculate_bmi(weight, height)}")
            pause()
        elif choice == "12":
            clear_screen()
            print("Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid option, please choose between 1 and 12.")
            pause()


def add_note(note):
    """Append a timestamped note to the notes file. Returns a confirmation string."""
    if not note:
        raise ValueError("Note cannot be empty")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {note}\n")

    return f"Note saved: {note}"


def get_notes():
    """Return a list of all saved notes (empty list if file doesn't exist)."""
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def get_weather(city):
    """Fetch current weather for a given city using wttr.in. Returns formatted string."""
    if not city:
        raise ValueError("City name cannot be empty")

    try:
        response = requests.get(f"https://wttr.in/{city}?format=%C+%t", timeout=5)
        response.raise_for_status()
        return f"Weather in {city}: {response.text.strip()}"
    except requests.RequestException:
        return f"Could not fetch weather for {city}. Check your internet connection."


def password_strength(password):
    """Rate a password as Weak, Medium, or Strong based on length and character variety."""
    if not password:
        raise ValueError("Password cannot be empty")

    length_ok = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([length_ok, has_upper, has_lower, has_digit, has_symbol])

    if score <= 2:
        return "Weak"
    elif score in (3, 4):
        return "Medium"
    else:
        return "Strong"


def get_time():
    """Return the current time as a string (HH:MM:SS)."""
    return datetime.now().strftime("%H:%M:%S")


def get_date():
    """Return today's date as a string (YYYY-MM-DD)."""
    return datetime.now().strftime("%Y-%m-%d")


def flip_coin():
    """Return 'Heads' or 'Tails' at random."""
    return random.choice(["Heads", "Tails"])


def roll_dice(sides=6):
    """Return a random integer between 1 and the given number of sides."""
    if sides < 2:
        raise ValueError("A dice must have at least 2 sides")
    return random.randint(1, sides)


def count_words(text):
    """Return the number of words in a given text."""
    if not text:
        return 0
    return len(text.split())


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit, rounded to 1 decimal."""
    return round((celsius * 9 / 5) + 32, 1)


def calculate_bmi(weight_kg, height_cm):
    """Calculate BMI given weight in kg and height in centimeters, rounded to 1 decimal."""
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Weight and height must be positive numbers")
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


if __name__ == "__main__":
    main()