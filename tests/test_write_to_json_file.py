import tempfile
from pathlib import Path
from typing import (
    Any,
    Dict,
    List,
)
from unittest.mock import (
    MagicMock,
    patch,
)

from core.main import write_to_json_file


def test_write_to_json_file(data_fields: List[Dict[str, Any]]):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        json_file_path = Path(tmp_file.name)

    mock_data = MagicMock()

    with patch('core.main.write_to_json_file', return_value=mock_data):
        write_to_json_file(data_fields, json_file_path)

        if not json_file_path.exists():
            raise AssertionError(
                f"Файл {json_file_path} не был создан.",
            )
