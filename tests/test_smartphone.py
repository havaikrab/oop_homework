from src.smartphone import Smartphone


def test_class_smartphone(attributes_smartphone_1: tuple) -> None:

    some_phone = Smartphone(*attributes_smartphone_1)
    assert some_phone.name == "Samsung Galaxy S23 Ultra"
    assert some_phone.description == "256GB, Серый цвет, 200MP камера"
    assert some_phone.price == 180000.0
    assert some_phone.quantity == 5
    assert some_phone.efficiency == 95.5
    assert some_phone.model == "S23 Ultra"
    assert some_phone.memory == 256
    assert some_phone.color == "Серый"
