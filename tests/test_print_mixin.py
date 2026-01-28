from typing import Any

from src.print_mixin import PrintMixin


def test_print_mixin_heritage(print_mixin_args: tuple, print_mixin_kwargs: dict, capsys: Any) -> None:
    class SomeTestClass(PrintMixin):
        def __init__(
            self,
            one: Any,
            two: Any,
            three: Any,
            four: Any,
            five: Any,
            six: Any,
            seven: Any = 7,
            eight: Any = 8,
            nine: Any = 9,
            ten: Any = 10,
        ):

            self.one = one
            self.two = two
            self.three = three
            self.four = four
            self.five = five
            self.six = six
            self.seven = seven
            self.eight = eight
            self.nine = nine
            self.ten = ten
            self._args = (one, two, three, four, five, six)
            self._kwargs = {"seven": seven, "eight": eight, "nine": nine, "ten": ten}
            super().__init__(*self._args, **self._kwargs)

    SomeTestClass(*print_mixin_args, **print_mixin_kwargs)
    console_message = capsys.readouterr()
    expected_part_1 = "SomeTestClass(1, '2', [3], (4.4, 'four'), {'5.5': 5}, 6, "
    expected_part_2 = "seven=(7, 7.7), eight=[8, 8.0], nine={9: 9.0}, ten=10)\n"
    assert console_message.out == expected_part_1 + expected_part_2
