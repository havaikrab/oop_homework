from typing import Any, Optional

from src.base_category import BaseCategory
from src.exceptions import NotPositiveQuantityError
from src.product import Product


class Category(BaseCategory):
    """Класс с описанием категории продуктов"""

    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: Any, description: Any, products: Optional[list] = None):
        """Метод инициализации экземпляра класса"""

        self.name: str = name
        self.description = description
        if products is None:
            self.__products = []
        else:
            for element in products:
                if not isinstance(element, Product):
                    raise TypeError(f"Класс переменной должен быть Product вместо {type(element)}")
                elif element.quantity <= 0:
                    raise NotPositiveQuantityError()
            self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Возвращает форматированную строку с названием категории
        и суммарным количеством продуктов, принадлежащих ей."""

        total_products_count = 0
        for product in self.__products:
            total_products_count += product.quantity
        return f"{self.name}, количество продуктов: {total_products_count} шт."

    @property
    def products(self) -> str:
        """Геттер приватного атрибута __products,
        возвращает каждый объект из списка продуктов категории в виде форматированной строки."""

        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result

    @property
    def products_list(self) -> list:
        """Геттер приватного атрибута __products, возвращает оригинальный список объектов-продуктов категории."""

        return self.__products

    def add_product(self, product: Any) -> None:
        """Метод добавления продукта в список продуктов категории"""

        if not isinstance(product, Product):
            raise TypeError(f"Класс переменной должен быть Product вместо {type(product)}")
        elif product.quantity <= 0:
            raise NotPositiveQuantityError("Попытка добавить продукт с неположительным количеством")

        update_status = False
        for element in self.__products:
            if element.name == product.name:
                element.quantity += product.quantity
                if element.price < product.price:
                    element.price = product.price
                update_status = True
                break
        if not update_status:
            self.__products.append(product)
            Category.product_count += 1

    def middle_price(self) -> float:
        """Метод, возвращающий среднюю цену продуктов, принадлежащих данной категории"""

        avg_price = 0.0
        try:
            return round(
                sum([product.price * product.quantity for product in self.__products])
                / sum([product.quantity for product in self.__products]),
                2,
            )
        except ZeroDivisionError:
            return avg_price
