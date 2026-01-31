from src.base_category import BaseCategory
from src.exceptions import NotPositiveQuantityError
from src.product import Product


class Order(BaseCategory):
    """Класс с описанием заказа продукта"""

    product: Product
    order_number = 1

    def __init__(self, name: str, description: str, product: Product):
        """Метод инициализации экземпляра класса"""

        self.name = name
        self.description = description
        if product.quantity <= 0:
            raise NotPositiveQuantityError("Заказ должен содержать хотя бы одну единицу продукта")
        self.product = product
        self.order_number = Order.order_number
        Order.order_number += 1
