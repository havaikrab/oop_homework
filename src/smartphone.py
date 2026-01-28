from src.product import Product


class Smartphone(Product):
    """Подкласс "Смартфон" класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Метод инициализации объекта класса Smartphone"""

        self._args = (name, description, price, quantity, efficiency, model, memory, color)
        super().__init__(*self._args)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
