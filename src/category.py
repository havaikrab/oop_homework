from typing import Any, Optional

from src.product import Product


class Category:
    """Класс с описанием категории продуктов"""

    name: str
    description: str
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
