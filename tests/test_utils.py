import json
from unittest.mock import mock_open, patch

from src import utils
from src.category import Category


mocked_data = mock_open(
    read_data=json.dumps(
        [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство коммуникации",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
                ],
            },
            {
                "name": "Телевизоры",
                "description": "Современный телевизор, который позволяет наслаждаться просмотром",
                "products": [
                    {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
                ],
            },
        ],
        indent=4,
        ensure_ascii=False,
    )
)


@patch("builtins.open", mocked_data)
def test_extract_categories() -> None:

    actual_category_count = Category.category_count
    actual_product_count = Category.product_count

    result = utils.extract_categories("some_file.json")
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
    assert result[0].description == "Смартфоны, как средство коммуникации"
    assert result[1].description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert result[0].products_list[0].name == "Samsung Galaxy C23 Ultra"
    assert result[1].products_list[0].name == '55" QLED 4K'
    assert result[0].products_list[1].description == "512GB, Gray space"
    assert result[1].products_list[0].description == "Фоновая подсветка"
    assert result[0].products_list[2].price == 31000.0
    assert result[1].products_list[0].price == 123000.0
    assert result[0].products_list[0].quantity == 5
    assert result[1].products_list[0].quantity == 7
    mocked_data.assert_called_once_with("some_file.json", "r", encoding="utf-8")

    Category.category_count = actual_category_count
    Category.product_count = actual_product_count
