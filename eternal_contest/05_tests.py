#!/usr/bin/env python3
"""
Во время разработки некоторой задачи Саша решил сгенерировать несколько новых тестов.
Каждый тест Саши должен представлять собой натуральное число, не меньшее l и не большее r.
Кроме того, натуральное число в тесте обязательно должно состоять из одинаковых цифр.

Например, число 999 подходит под это требование, а число 123 — нет.
Какое максимальное число различных тестов сможет создать Саша?

Limitations
-----------
* time - 1 s.
* memory - 256 MB.

Input
-----
В единственной строке вводятся два натуральных числа:

* 1 <= l <= 1e18;
* 1 <= r <= 1e18.

Обратите внимание: если эти числа не вместятся в 32-битный тип данных,
используйте 64-битный при необходимости.

Output
------
Выведите одно число — количество тестов, которое может сделать Саша.

Examples
--------
Ex1:
Input:
4 7
Output:
4

Ex2:
Input:
10 100
Output:
9

Notes
-----

В первом тесте Саше подходят номера [4,5,6,7].

Во втором тесте подходят все числа, кратные 11, от 11 до 99.
"""


from typing import Generator


def get_length(num: int) -> int:
    """Returns the amount of digits in the num."""
    return len(str(num))


def gen_unichars(
    length: int, base: str
) -> Generator[str, None, None]:
    """Generates a string composed of a base character times length."""
    for char in base:
        yield char * length


def count_tests(low: int, high: int) -> int:
    """Solves the problem."""
    lowlen, highlen = map(get_length, (low, high))
    digits = "123456789"
    total = 0 if low else 1
    for leng in range(lowlen, highlen + 1):
        total += len(
            [
                num
                for num in gen_unichars(leng, digits)
                if low <= int(num) <= high
            ]
        )
    return total


if __name__ == "__main__":
    left, right = map(int, input().split())
    left, right = min(left, right), max(left, right)
    print(count_tests(left, right))
