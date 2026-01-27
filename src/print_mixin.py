class PrintMixin:
    """Класс, расширяющий функционал основных рабочих классов, посредством вывода соответствующего сообщения
    при инициализации нового объекта этих классов."""

    def __init__(self) -> None:
        """Метод, выводящий информацию об инициализации нового объекта класса"""

        print(repr(self))

    def __repr__(self) -> str:
        """Метод, возвращающий строку, соответствующую строке кода, инициализирующего новый объект класса Product"""

        result_part_1 = f"{self.__class__.__name__}"
        result_part_2 = f"('{self.name}', '{self.description}', {self.price}, {self.quantity})"  # type: ignore
        return result_part_1 + result_part_2
