# JarvisCLI - Personal Terminal Assistant

#### Video URL: <YouTube video havolasini shu yerga qo'yasiz>

#### Description:
JarvisCLI is a lightweight, interactive command-line interface (CLI) personal assistant written in Python. It was developed as the final project for Harvard University's CS50's Introduction to Programming with Python (CS50P) course.

The goal of JarvisCLI is to provide a single, clean terminal interface where users can perform everyday utility tasks without needing complex desktop GUIs or multiple web browsers.

### Features Overview

1. **Note Taking System (`add_note`, `get_notes`)**
   Allows users to write quick text notes. Each note is saved with an automatic timestamp (`YYYY-MM-DD HH:MM`) into a local file named `notes.txt`. Users can view all saved notes anytime.

2. **Weather Checking (`get_weather`)**
   Fetches live weather reports for any city using the open `wttr.in` service via HTTP requests (`requests` library). It handles network connection errors gracefully.

3. **Password Strength Meter (`password_strength`)**
   Evaluates user passwords based on length, presence of uppercase letters, lowercase letters, digits, and special characters, returning ratings: "Weak", "Medium", or "Strong".

4. **Unit & Health Utilities (`celsius_to_fahrenheit`, `calculate_bmi`, `count_words`)**
   - Quick temperature conversions from Celsius to Fahrenheit.
   - Body Mass Index (BMI) calculator based on weight in kilograms and height in centimeters.
   - Word counter utility to inspect text length.

5. **Randomizers & Time Tools (`flip_coin`, `roll_dice`, `get_time`, `get_date`)**
   - Virtual coin flipper and customizable N-sided dice roller.
   - Quick displays for current system time and date.

### File Structure & Project Architecture

- **`project.py`**: Contains the primary entry point `main()` along with all the standalone utility functions. The program uses a clean terminal clearing function to present a responsive menu-driven UI.
- **`test_project.py`**: Contains automated tests using `pytest` to test core logic functions including password scoring, BMI calculations, unit conversions, and input validations.
- **`requirements.txt`**: Lists external Python packages required to run the application (e.g., `requests`).
- **`README.md`**: Detailed documentation of the project structure and setup instructions.

### Design Decisions

During development, modular design principles were emphasized. Each functionality (e.g., calculation, fetching external data, file I/O) is separated into its own pure or helper function. This separation ensured that functions could be tested independently using `pytest` without triggering CLI `input()` loops or user interactions.

Custom exception handling was added for inputs (e.g., negative height/weight in BMI or non-positive sides in dice rolling) to prevent the program from crashing abruptly during operation.