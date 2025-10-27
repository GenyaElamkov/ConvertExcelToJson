from pathlib import Path
from unittest.mock import (
    MagicMock,
    patch,
)

from core.main import file_exists


def test_file_exists_success():
    mock_wb = MagicMock()
    with patch("core.main.load_workbook", return_value=mock_wb):
        result = file_exists(Path("dummy.xlsx"))
        assert result == mock_wb


def test_file_exists_not_found():
    with patch("core.main.load_workbook", side_effect=FileNotFoundError()):
        result = file_exists(Path("nonexistent.xlsx"))
        assert result is None
