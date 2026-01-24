from src.category import Category


class Iterator:
    """Класс перебора объектов класса Product, входящих в объект класса Category"""

    def __init__(self, category_object: Category):
        """Метод инициализации объекта класса, принимает объект класса Category"""

        if not isinstance(category_object, Category):
            raise TypeError(f"Аргумент должен быть класса Category вместо {type(category_object)}")
        self.object = category_object
        self.stop = len(category_object.products_list)

    def __iter__(self) -> "Iterator":
        """Метод, возвращающий итератор из списка продуктов аргумента в виде строк"""

        self.product_index = -1
        return self

    def __next__(self) -> str:
        """Метод, возвращающий очередной элемент из списка продуктов аргумента"""

        if self.product_index < self.stop - 1:
            self.product_index += 1
            return str(self.object.products_list[self.product_index])
        else:
            raise StopIteration
