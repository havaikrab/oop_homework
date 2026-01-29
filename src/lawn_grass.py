from src.product import Product


class LawnGrass(Product):
    """Подкласс "Трава газонная" класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Метод инициализации объекта класса LawnGrass"""

        self._args = (name, description, price, quantity, country, germination_period, color)
        super().__init__(*self._args)
        self.country = country
        self.germination_period = germination_period
        self.color = color
