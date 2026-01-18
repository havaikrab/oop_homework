from typing import Optional

from src.product import Product


class Category:
    """Класс с описанием категории продуктов"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        """Метод инициализации экземпляра класса"""

        self.name = name
        self.description = description
        if products is None:
            products = []
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        """Геттер приватного атрибута __products,
        возвращает каждый объект из списка продуктов категории в виде форматированной строки."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def add_product(self, product: Product) -> None:
        """Метод добавления продукта в список продуктов категории.
        Если в категории уже существует добавляемый продукт,
        то количество существующего объекта увеличивается на значение количества добавляемого объекта."""

        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1
        else:
            self.__products[self.__products.index(product)].quantity += product.quantity
