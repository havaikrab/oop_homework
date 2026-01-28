from typing import Any


class PrintMixin:
    """Класс, расширяющий функционал основных рабочих классов, посредством вывода соответствующего сообщения
    при инициализации нового объекта этих классов."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Метод, выводящий информацию об инициализации нового объекта класса"""

        self._args = args
        self._kwargs = kwargs
        print(repr(self))

    def __repr__(self) -> str:
        """Метод, возвращающий строку, соответствующую строке кода, инициализирующего данный объект"""

        result_str = f"{self.__class__.__name__}("
        result_list = list()
        for i in self._args:
            if isinstance(i, str):
                result_list.append(f"'{i}'")
            else:
                result_list.append(f"{i}")
        for k, v in self._kwargs.items():
            result_list.append(f"{k}={v}")
        result_str += ", ".join(result_list) + ")"
        return result_str
