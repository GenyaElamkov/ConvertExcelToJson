from unittest.mock import MagicMock

from openpyxl.workbook import Workbook

from core.main import get_data_from_excel


def test_get_data_from_excel_normal_case():
    """Тест нормального извлечения данных с несколькими строками"""
    wb = MagicMock(spec=Workbook)
    ws = MagicMock()
    wb.active = ws

    # Настройка заголовков
    headers = ['Имя', 'Возраст']
    first_row_cells = [MagicMock(value=h) for h in headers]
    ws.__getitem__.return_value = first_row_cells

    # Настройка строк данных
    ws.max_row = 3  # 1 строка заголовков + 2 строки данных

    def cell_side_effect(row, column):
        if row == 2:
            return MagicMock(value=['Алиса', 30][column-1])
        elif row == 3:
            return MagicMock(value=['Боб', 25][column-1])
        raise ValueError(f"Неожиданная строка {row}")

    ws.cell.side_effect = cell_side_effect

    result = get_data_from_excel(wb)
    assert result == [{'Имя': 'Алиса', 'Возраст': 30}, {'Имя': 'Боб', 'Возраст': 25}]


def test_get_data_from_excel_missing_values():
    """Тест обработки отсутствующих значений в ячейках"""
    wb = MagicMock(spec=Workbook)
    ws = MagicMock()
    wb.active = ws

    headers = ['Логин', 'Рейтинг']
    first_row_cells = [MagicMock(value=h) for h in headers]
    ws.__getitem__.return_value = first_row_cells
    ws.max_row = 2

    def cell_side_effect(row, column):
        if row == 2:
            return MagicMock(value=[None, 95][column-1])
        raise ValueError(f"Неожиданная строка {row}")

    ws.cell.side_effect = cell_side_effect

    result = get_data_from_excel(wb)
    assert result == [{'Логин': None, 'Рейтинг': 95}]
