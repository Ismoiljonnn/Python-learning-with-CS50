from seasons import calculate_minutes, validate_date
from datetime import date
import pytest

def test_calculate_minutes():
    assert calculate_minutes(date(2025, 6, 12), date(2026, 6, 12)) == 525600
    assert calculate_minutes(date(2023, 6, 12), date(2024, 6, 12)) == 527040

def test_invalid_input():
    with pytest.raises(SystemExit):
        validate_date("January 1st, 2000")
    with pytest.raises(SystemExit):
        validate_date("2026-13-45")