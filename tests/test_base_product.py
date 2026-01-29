from src.base_product import BaseProduct


def test_base_product_heritage() -> None:  # Тест для строки №10 модуля base_product.py
    class TestProduct(BaseProduct):  # Написан, чтобы сохранить 100% покрытие тестами :))
        def __init__(self, something: str) -> None:
            super().__init__()  # type: ignore
            self.something = something

    some_object = TestProduct("something")
    assert some_object.something == "something"
