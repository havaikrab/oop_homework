from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """Абстрактный класс разделения продуктов по категориям и группам"""

    name: str
    description: str

    @abstractmethod
    def __init__(self, *args: tuple, **kwargs: dict):
        """Абстрактный метод инициализации класса-наследника BaseCategory"""
        pass
