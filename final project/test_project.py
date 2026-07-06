"""
Tests for project.py (JarvisCLI)

Run with: pytest test_project.py
"""

import os
import pytest
from project import (
    add_note,
    get_notes,
    get_weather,
    password_strength,
    get_time,
    get_date,
    flip_coin,
    roll_dice,
    count_words,
    celsius_to_fahrenheit,
    calculate_bmi,
    NOTES_FILE,
)


def setup_function():
    """Runs before each test: make sure notes.txt is clean."""
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)


def teardown_function():
    """Runs after each test: clean up notes.txt."""
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)


def test_add_note():
    result = add_note("Buy groceries")
    assert "Buy groceries" in result
    assert "Note saved" in result

    with pytest.raises(ValueError):
        add_note("")


def test_get_notes():
    assert get_notes() == []  # no notes yet

    add_note("First note")
    add_note("Second note")
    notes = get_notes()

    assert len(notes) == 2
    assert "First note" in notes[0]
    assert "Second note" in notes[1]


def test_password_strength():
    assert password_strength("abc") == "Weak"
    assert password_strength("abcdefgH") == "Medium"
    assert password_strength("Abcdef12") == "Medium"
    assert password_strength("Abcd12!@") == "Strong"

    with pytest.raises(ValueError):
        password_strength("")


def test_get_weather_invalid_input():
    # We only test input validation here, not the live API call,
    # since network responses are not reliable to test against.
    with pytest.raises(ValueError):
        get_weather("")


def test_get_time_and_date():
    # Just check the format, since the exact value always changes.
    assert len(get_time().split(":")) == 3  # HH:MM:SS
    assert len(get_date().split("-")) == 3  # YYYY-MM-DD


def test_flip_coin():
    for _ in range(20):
        assert flip_coin() in ("Heads", "Tails")


def test_roll_dice():
    for _ in range(20):
        result = roll_dice(6)
        assert 1 <= result <= 6

    with pytest.raises(ValueError):
        roll_dice(1)


def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("") == 0
    assert count_words("CS50P is fun") == 3


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == 98.6


def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.9

    with pytest.raises(ValueError):
        calculate_bmi(0, 1.75)
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)