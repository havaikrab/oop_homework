from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для создания классов-наследников"""

    @abstractmethod
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        """Абстрактный метод инициализации объекта класса-наследника BaseProduct"""
        pass
