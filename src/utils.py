import json

from src.category import Category
from src.product import Product


def extract_categories(path_to_file: str) -> list:
    """Принимает строку имени JSON-файла и пути к нему.
    Возвращает список категорий товаров в виде объектов класса Category.
    Каждая категория имеет список товаров, представленных в виде объектов класса Product"""

    with open(path_to_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories_list = list()
    for element in data:
        category_name = element.get("name")
        category_description = element.get("description")
        category_products = list()
        for item in element.get("products"):
            product_name = item.get("name")
            product_description = item.get("description")
            product_price = item.get("price")
            product_quantity = item.get("quantity")
            category_products.append(Product(product_name, product_description, product_price, product_quantity))
        categories_list.append(Category(category_name, category_description, category_products))
    return categories_list
