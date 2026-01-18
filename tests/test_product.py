from src import product


def test_class_prodict(product_attributes: tuple) -> None:
    some_phone = product.Product(*product_attributes)
    assert some_phone.name == "Iphone 15"
    assert some_phone.description == "512GB, Gray space"
    assert some_phone.price == 210000.0
    assert some_phone.quantity == 8
