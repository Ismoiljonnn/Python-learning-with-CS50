"""
Tests for project.py (JarvisCLI)

Run with: pytest test_project.py
"""

import os
import pytest
from project import add_note, get_notes, get_weather, password_strength, NOTES_FILE


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