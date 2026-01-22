import pytest

from src.category import Category
from src.product import Product


def test_class_category(
    product_phone1: Product,
    product_another_phone1: Product,
    product_phone2: Product,
    category_attributes_phones: list,
    category_attributes_tv: list,
) -> None:

    actual_category_count = Category.category_count
    actual_product_count = Category.product_count

    phones_dict = {"products": [product_phone1, product_another_phone1, product_phone2]}
    phones = Category(*category_attributes_phones, **phones_dict)
    assert phones.name == "Смартфоны"
    assert phones.description == "Неотъемлемый атрибут современного человека"
    assert phones.products.strip().split("\n") == [
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Iphone 15, 300000.0 руб. Остаток: 5 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]
    assert Category.category_count == actual_category_count + 1
    assert Category.product_count == actual_product_count + 3

    tv = Category(*category_attributes_tv)
    assert tv.name == "Телевизоры"
    assert tv.description == "Источник хорошего настроения"
    assert tv.products == ""
    assert Category.category_count == actual_category_count + 2
    assert Category.product_count == actual_product_count + 3

    Category.category_count = actual_category_count
    Category.product_count = actual_product_count


def test_class_category_invalid_product_list(category_attributes_phones: tuple, phone_names_list: list) -> None:
    with pytest.raises(TypeError):
        assert Category(category_attributes_phones[0], category_attributes_phones[1], phone_names_list)


def test_category_add_invalid_product(category_attributes_phones: tuple, attributes_phone1: tuple) -> None:
    phones = Category(*category_attributes_phones)
    with pytest.raises(TypeError):
        phones.add_product(attributes_phone1)


def test_category_add_product(
    product_phone1: Product,
    product_another_phone1: Product,
    product_phone2: Product,
    product_another_phone2: Product,
    category_attributes_phones: tuple,
) -> None:

    phones = Category(*category_attributes_phones)
    phones.add_product(product_phone1)
    assert phones.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    assert phones.products_list[0].description == "512GB, Gray space"
    phones.add_product(product_phone2)
    phones.add_product(product_another_phone1)
    assert phones.products.strip().split("\n") == [
        "Iphone 15, 300000.0 руб. Остаток: 13 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]
    assert phones.products_list[0].description == "512GB, Gray space"
    phones.add_product(product_another_phone2)
    assert phones.products.strip().split("\n") == [
        "Iphone 15, 300000.0 руб. Остаток: 13 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 15 шт.",
    ]
    assert phones.products_list[1].description == "1024GB, Синий"
