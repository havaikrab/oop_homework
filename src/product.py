class Product:
    """Класс с описанием продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод инициализации экземпляра класса"""

        if (
            not isinstance(name, str)
            or not isinstance(description, str)
            or not isinstance(price, float | int)
            or not isinstance(quantity, int)
        ):
            raise TypeError("Тип данных аргумента не соответствует ожидаемому")
        elif price <= 0:
            raise ValueError("Цена не может быть меньше или равной нулю!")
        elif quantity < 0:
            raise ValueError("Количество не может быть меньше нуля!")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает форматированную строку с названием, ценой и количеством продукта"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        """Геттер приватного атрибута __price, возвращает значение цены продукта."""

        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер приватного атрибута __price, позволяет изменить цену продукта,
        только, если значение новой цены больше нуля"""

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price <= new_price:
            self.__price = new_price
        else:
            print(
                """Новая цена продукта меньше текущей. Если вы согласны с понижением цены,
введите английскую "y", иначе, введите любой другой символ или нажмите Enter."""
            )
            user_accept = input().lower()
            if user_accept == "y":
                self.__price = new_price
            print(f"Установлена цена продукта: {self.__price} руб.")

    @classmethod
    def new_product(cls, product_from_dict: dict) -> "Product":
        """Метод для создания объекта класса из параметров, указанных в виде словаря"""

        name = product_from_dict.get("name")
        description = product_from_dict.get("description")
        price = product_from_dict.get("price", 0.0)
        quantity = product_from_dict.get("quantity", 0)
        if name and description:
            product = cls(name, description, price, quantity)
            return product
        else:
            raise ValueError("Аргумент не содержит ожидаемых параметров")
