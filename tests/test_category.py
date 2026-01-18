from src import category
from src.category import Category


def test_class_category(category_attributes_phones: tuple, category_attributes_tv: tuple) -> None:

    actual_category_count = Category.category_count
    actual_product_count = Category.product_count

    phones = category.Category(*category_attributes_phones)
    assert phones.name == "Смартфоны"
    assert phones.description == "Неотъемлемый атрибут современного человека"
    assert phones.products == ["Samsung", "Xiaomi", "Iphone"]
    assert Category.category_count == actual_category_count + 1
    assert Category.product_count == actual_product_count + 3

    tv = category.Category(*category_attributes_tv)
    assert tv.name == "Телевизоры"
    assert tv.description == "Источник хорошего настроения"
    assert tv.products == []
    assert Category.category_count == actual_category_count + 2
    assert Category.product_count == actual_product_count + 3

    Category.category_count = actual_category_count
    Category.product_count = actual_product_count
