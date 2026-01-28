from src.base_category import BaseCategory


def test_base_category_heritage() -> None:  # Тест для строки №13 модуля base_category.py
    class TestCategory(BaseCategory):  # Написан, чтобы сохранить 100% покрытие тестами :))
        def __init__(self, name: str, description: str) -> None:
            super().__init__()  # type: ignore
            self.name = name
            self.description = description

    some_category = TestCategory("Категория", "Описание категории")
    assert some_category.name == "Категория"
    assert some_category.description == "Описание категории"
