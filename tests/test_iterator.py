import pytest

from src.category import Category
from src.iterator import Iterator
from src.product import Product


def test_iterator_invalid_type(phone_names_list: list) -> None:
    with pytest.raises(TypeError):
        Iterator(phone_names_list)  # type: ignore


def test_iterator_phones(category_attributes_phones: tuple, product_phone1: Product, product_phone2: Product) -> None:
    phones_list = [product_phone1, product_phone2]
    phones_category = Category(category_attributes_phones[0], category_attributes_phones[1], phones_list)
    phones_iterator = iter(Iterator(phones_category))
    assert next(phones_iterator) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert next(phones_iterator) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    with pytest.raises(StopIteration):
        next(phones_iterator)
