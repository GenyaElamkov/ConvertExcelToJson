from datetime import datetime

import pytest

from core.main import convert_date_to_string


@pytest.mark.parametrize(
    "date, expected", [
        (datetime(1900, 1, 1, 0, 0), "1900-01-01"),
        (datetime(2025, 1, 1, 0, 0), "2025-01-01"),
    ],
)
def test_convert_date_to_string_normal_case(date, expected):
    """Тест нормального преобразования даты в строку"""
    result = convert_date_to_string(date)
    assert result == expected
