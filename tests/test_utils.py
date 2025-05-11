import json
from typing import Any
from unittest.mock import MagicMock, mock_open, patch

from src.classes import Category
from src.utils import get_products_from_json, add_products


def test_get_transactions_from_valid_file(products_list: list[dict[str, Any]]) -> None:
    mock_data = json.dumps(products_list)
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_products_from_json("dummy_path.json")
        assert result == products_list


def test_get_transactions_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError()):
        result = get_products_from_json("not_found.json")
        assert result == []


def test_get_transactions_invalid_json() -> None:
    with (
        patch("builtins.open", mock_open(read_data="INVALID_JSON")),
        patch("json.load", side_effect=json.JSONDecodeError("msg", "", 0)),
    ):
        result = get_products_from_json("invalid.json")
        assert result == []


def test_get_transactions_invalid_structure() -> None:
    bad_structure = json.dumps({"not": "a list"})
    with patch("builtins.open", mock_open(read_data=bad_structure)):
        result = get_products_from_json("bad_struct.json")
        assert result == []


def test_get_transactions_wtf_error() -> None:
    with patch("builtins.open", mock_open(read_data="{}")), \
            patch("json.load", side_effect=TypeError("boom!")):
        result = get_products_from_json("broken.json")
        assert result == []  # проверяем, что функция вернула [] при исключении


def test_add_products(products_list: list[dict]) -> None:
    Category.category_count = 0
    Category.product_count = 0
    categories = add_products(products_list)
    assert Category.category_count == 2
    assert Category.product_count == 4
