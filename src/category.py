from typing import Optional


class Category:
    """Класс с описанием категории продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        """Метод инициализации экземпляра класса"""

        self.name = name
        self.description = description
        if products is None:
            products = []
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
