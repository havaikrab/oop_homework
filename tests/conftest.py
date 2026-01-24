import pytest

from src.product import Product


@pytest.fixture
def attributes_phone1() -> tuple:
    return "Iphone 15", "512GB, Gray space", 210000.0, 8


@pytest.fixture
def product_phone1() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_another_phone1() -> Product:
    return Product("Iphone 15", "Такой же Iphone 15 только лучше", 300000.0, 5)


@pytest.fixture
def product_phone2() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product_another_phone2() -> Product:
    return Product("Xiaomi Redmi Note 11", "Такой же Xiaomi только дешевле", 25000.0, 1)


@pytest.fixture
def category_attributes_phones() -> tuple:
    return "Смартфоны", "Неотъемлемый атрибут современного человека"


@pytest.fixture
def category_attributes_tv() -> tuple:
    return "Телевизоры", "Источник хорошего настроения"


@pytest.fixture
def phone_names_list() -> list:
    return ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]


@pytest.fixture
def attributes_grass_1() -> tuple:
    return "Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый"


@pytest.fixture
def attributes_smartphone_1() -> tuple:
    return "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
