from pathlib import Path
from unittest.mock import (
    MagicMock,
    patch,
)

from core.main import load_workbook_safe


def test_load_workbook_safe_success():
    mock_wb = MagicMock()
    with patch("core.main.load_workbook", return_value=mock_wb):
        result = load_workbook_safe(Path("dummy.xlsx"))
        assert result == mock_wb


def test_load_workbook_safe_not_found():
    with patch("core.main.load_workbook", side_effect=FileNotFoundError()):
        result = load_workbook_safe(Path("nonexistent.xlsx"))
        assert result is None
