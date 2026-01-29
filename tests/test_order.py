import pytest

from src.exceptions import NotPositiveQuantityError
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


def test_class_order(some_order_attributes: tuple, product_another_phone1: Product) -> None:

    actual_order_number = Order.order_number

    some_order = Order(some_order_attributes[0], some_order_attributes[1], product_another_phone1)
    assert some_order.name == "Покупка"
    assert some_order.description == "Покупка телефона"
    assert some_order.product.name == "Iphone 15"
    assert some_order.product.description == "Такой же Iphone 15 только лучше"
    assert some_order.product.price == 300000.0
    assert some_order.product.quantity == 5
    assert some_order.order_number == actual_order_number

    Order.order_number = actual_order_number


def test_not_positive_product_quantity(smartphone_1: Smartphone) -> None:
    smartphone_1.quantity = -10
    with pytest.raises(NotPositiveQuantityError, match="Заказ должен содержать хотя бы одну единицу продукта"):
        Order("Покупка телефона", "Онлайн-покупка смартфона", smartphone_1)
