from typing import Any
from unittest.mock import patch

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_class_prodict(attributes_phone1: tuple) -> None:
    some_phone = Product(*attributes_phone1)
    assert some_phone.name == "Iphone 15"
    assert some_phone.description == "512GB, Gray space"
    assert some_phone.price == 210000.0
    assert some_phone.quantity == 8


@pytest.mark.parametrize(
    "params",
    [
        ({"name": None, "description": "Что-то безымянное", "price": 100.0, "quantity": 5}),
        ({"name": "Что-то", "description": None, "price": 200.0, "quantity": 10}),
        ({"name": "Еще что-то", "description": "Описание еще чего-то", "price": 333, "quantity": 3.3}),
    ],
)
def test_create_product_invalid_argument_type(params: dict) -> None:
    with pytest.raises(TypeError):
        assert Product(**params)


@pytest.mark.parametrize(
    "params",
    [
        ({"name": "Что-то", "description": "Описание чего-то", "price": 0, "quantity": 10}),
        ({"name": "Еще что-то", "description": "Описание еще чего-то", "price": 333, "quantity": -1}),
    ],
)
def test_create_product_invalid_argument_value(params: dict) -> None:
    with pytest.raises(ValueError):
        assert Product(**params)


def test_price_setter_invalid_value(capsys: Any, product_phone1: Product) -> None:
    product_phone1.price = 0
    console_message = capsys.readouterr()
    assert product_phone1.price == 210000.0
    assert console_message.out == "Цена не должна быть нулевая или отрицательная\n"


@patch("builtins.input")
def test_price_setter_accept_price_lower(mock_accept: Any, product_phone2: Product, capsys: Any) -> None:
    mock_accept.return_value = "y"
    product_phone2.price = 100
    console_message = capsys.readouterr()
    assert product_phone2.price == 100
    assert console_message.out.strip().split("\n") == [
        "Новая цена продукта меньше текущей. Если вы согласны с понижением цены,",
        'введите английскую "y", иначе, введите любой другой символ или нажмите Enter.',
        "Установлена цена продукта: 100 руб.",
    ]


@patch("builtins.input")
def test_price_setter_reject_price_lower(mock_accept: Any, product_phone1: Product, capsys: Any) -> None:
    mock_accept.return_value = "n"
    product_phone1.price = 100
    console_message = capsys.readouterr()
    assert product_phone1.price == 210000.0
    assert console_message.out.strip().split("\n") == [
        "Новая цена продукта меньше текущей. Если вы согласны с понижением цены,",
        'введите английскую "y", иначе, введите любой другой символ или нажмите Enter.',
        "Установлена цена продукта: 210000.0 руб.",
    ]


@pytest.mark.parametrize(
    "product_dict, expected_list",
    [
        (
            {"name": "Что-то", "description": "Что-то тестовое", "price": 100, "quantity": 5},
            ["Что-то", "Что-то тестовое", 100.0, 5],
        ),
        (
            {"name": "Еще что-то", "description": "Опять что-то тестовое", "price": 99.99},
            ["Еще что-то", "Опять что-то тестовое", 99.99, 0],
        ),
    ],
)
def test_new_product(product_dict: dict, expected_list: list) -> None:
    some_product = Product.new_product(product_dict)
    assert [some_product.name, some_product.description, some_product.price, some_product.quantity] == expected_list


@pytest.mark.parametrize(
    "product_dict",
    [
        ({"name": None, "description": "Что-то безымянное", "price": 100, "quantity": 5}),
        ({"name": "Что-то неопределенное", "description": None, "price": 99.99, "quantity": 3}),
        ({"name": "Еще что-то", "description": "Что-то бесценное", "quantity": 10}),
    ],
)
def test_new_product_invalid_values(product_dict: dict) -> None:
    with pytest.raises(ValueError):
        Product.new_product(product_dict)


def test_product_add_invalid_type(product_phone1: Product) -> None:
    with pytest.raises(TypeError):
        product_phone1 + "Другой телефон"  # type: ignore


def test_product_add_invalid_subclass(smartphone_1: Smartphone, grass_1: LawnGrass) -> None:
    with pytest.raises(TypeError):
        smartphone_1 + grass_1


def test_product_add(product_phone2: Product, product_another_phone2: Product) -> None:
    assert product_phone2 + product_another_phone2 == 459000.0
