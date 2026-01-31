from typing import Optional


class NotPositiveQuantityError(Exception):
    """Класс исключений, возбуждаемых при попытке передать в какой-либо подкласс класса BaseCategory
    объект класса Product, имеющий неположительное значение атрибута quantity"""

    def __init__(self, message: Optional[str] = None) -> None:
        """Метод инициализации объекта исключения"""

        if not message:
            self.message = "Объект класса Product имеет неположительное значение атрибута quantity"
        else:
            self.message = message

    def __str__(self) -> str:
        """Метод строкового представления объекта исключения"""

        return self.message
