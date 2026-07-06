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
    print("5. Exit")
    print("-" * 30)


def pause():
    """Wait for the user to press Enter before returning to the menu."""
    input("\nPress Enter to return to the menu...")


def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

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
            clear_screen()
            print("Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid option, please choose between 1 and 5.")
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


if __name__ == "__main__":
    main()