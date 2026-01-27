from src.lawn_grass import LawnGrass


def test_class_lawn_grass(attributes_grass_1: tuple) -> None:

    some_grass = LawnGrass(*attributes_grass_1)
    assert some_grass.name == "Газонная трава"
    assert some_grass.description == "Элитная трава для газона"
    assert some_grass.price == 500.0
    assert some_grass.quantity == 20
    assert some_grass.country == "Россия"
    assert some_grass.germination_period == "7 дней"
    assert some_grass.color == "Зеленый"
