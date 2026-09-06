# JarvisCLI - Personal Terminal Assistant

#### Video Demo: https://youtu.be/Phvvx3c4CTI?si=BVW9nVyhHNCWOrAt

#### Description:

JarvisCLI is a lightweight, interactive command-line interface (CLI) personal assistant written in Python. It was developed as the final project for Harvard University's CS50's Introduction to Programming with Python (CS50P) course. The primary goal of JarvisCLI is to provide a unified, fast, and clean terminal experience where users can perform everyday utility tasks—such as taking quick notes, checking weather forecasts, evaluating password security, and performing basic unit conversions—without needing to switch context or open web browsers.

### Features Overview

The application provides a comprehensive suite of utilities accessible through an intuitive menu system:

1. **Note-Taking System (`add_note`, `get_notes`)**
   Allows users to append text notes to a local persistent file (`notes.txt`). Each entry is automatically stamped with the current date and time (`YYYY-MM-DD HH:MM`). Users can retrieve and review all saved notes directly within the terminal interface at any time.

2. **Weather Checking (`get_weather`)**
   Fetches real-time weather reports for any specified city using the open `wttr.in` service via HTTP GET requests (powered by the `requests` library). It safely handles connection timeouts and network errors gracefully.

3. **Password Strength Meter (`password_strength`)**
   Analyzes password security using regular expressions (`re` module). It evaluates length, presence of uppercase and lowercase letters, numeric digits, and special characters, categorizing the password as "Weak", "Medium", or "Strong".

4. **Randomizers & Utilities (`flip_coin`, `roll_dice`)**
   Provides utility tools including a virtual coin flipper, an N-sided customizable dice roller with boundary validations, a word counter for input text, temperature conversion (Celsius to Fahrenheit), and a Body Mass Index (BMI) calculator.

5. **Time and Date Helpers (`get_time`, `get_date`)**
   Instantly displays system time and date formatted for quick readability.

### Project Architecture & File Structure

- **`project.py`**: This serves as the primary entry point of the application. It contains the interactive loop within `main()` that renders the main menu, parses user choices, and invokes individual helper functions. All functional utilities (such as weather fetching, note appending, password checking, and math operations) are modularized into independent standalone functions.
- **`test_project.py`**: Contains automated unit tests written using the `pytest` framework. It thoroughly tests the core logic functions (e.g., `password_strength`, `count_words`, `celsius_to_fahrenheit`, `calculate_bmi`, and `roll_dice`) including edge cases and exception handling (like catching `ValueError` on invalid inputs).
- **`requirements.txt`**: Lists external Python dependencies required to run the project, such as `requests` and `pytest`.
- **`README.md`**: Detailed documentation explaining the project overview, structure, design decisions, and usage instructions.

### Design Decisions

During the architecture phase of JarvisCLI, a primary focus was put on modularity and testability. To strictly adhere to CS50P guidelines, functions responsible for core logic (like calculating BMI or parsing strings) were kept completely separated from I/O operations like `input()` and `print()`. This design choice ensured that every function could be easily tested via `pytest` without triggering interactive prompts. 

For the weather module, using `wttr.in` was selected over complex APIs requiring API keys to keep the setup minimal and friction-free for end users. Error handling was implemented extensively across all input prompts to prevent the CLI from crashing on invalid user input.

### How to Run and Test

To start the CLI assistant:
```bash
python project.py