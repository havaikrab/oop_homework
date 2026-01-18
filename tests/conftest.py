import pytest


@pytest.fixture
def product_attributes() -> tuple:
    return "Iphone 15", "512GB, Gray space", 210000.0, 8


@pytest.fixture
def category_attributes_phones() -> tuple:
    return "Смартфоны", "Неотъемлемый атрибут современного человека", ["Samsung", "Xiaomi", "Iphone"]


@pytest.fixture
def category_attributes_tv() -> tuple:
    return "Телевизоры", "Источник хорошего настроения"
