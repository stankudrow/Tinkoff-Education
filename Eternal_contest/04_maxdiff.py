#!/usr/bin/env python3
"""
У Кости есть бумажка, на которой написано n чисел.
Также у него есть возможность не больше, чем k раз,
взять любое число с бумажки, после чего закрасить одну из старых цифр,
а на её месте написать новую произвольную цифру.

На какое максимальное значение Костя сможет увеличить сумму всех чисел на листочке?

Limitations
-----------
* time - 2 s.
* memory - 256 MB.

Input
-----
В первой строке входного файла даны два целых числа:
* n (1 <= n <= 1e3) — количество чисел на бумажке; 
* k (1 <= n <= 1e4) — ограничение на число операций. 

Во второй строке записано n чисел a_i (1 <= a_i <= 1e9).

Output
------
Выведите максимальную разность между конечной и начальной суммой.

Examples
--------
Ex1:
Input:
5  2
1  2  1  3  5
Output:
16

Ex2:
Input:
3  1
99  5  85
Output:
10

Ex3:
Input:
1  10
9999
Output:
0

Notes
-----

В первом примере Костя может изменить две единицы на две девятки,
в результате чего сумма чисел увеличится на 16.

Во втором примере Костя меняет число 85 на 95.

В третьем примере можно ничего не менять.

Обратите внимание, что ответ может превышать вместимость 32-битного типа данных.
"""


from collections import defaultdict
from typing import Iterable, List, Tuple


def dissect(
    numbers: Iterable[int | str],
) -> Tuple[dict[int, List[int]], List[int], int]:
    """Dissects incoming numbers.

    Returns
    -------
    Tuple[dict[int, List[int]], List[int], int]
        0. the positions of digits with the digits from the numbers
        1. the sorted positions with ascending weights (units->decimals->...)
        2. the total amount of digits processed.
    """
    posdigits: dict[int, List[int]] = defaultdict(list)
    ndigits: int = 0
    for number in numbers:
        numstr = str(number)
        if numstr.isdigit():
            for pos, digit in enumerate(reversed(numstr)):
                if digit != "9":
                    posdigits[pos].append(int(digit))
                    ndigits += 1
    positions = sorted(posdigits.keys())
    return (
        {
            pos: sorted(posdigits[pos], reverse=True)
            for pos in positions
        },
        positions,
        ndigits,
    )


if __name__ == "__main__":
    _, nops = map(int, input().split())
    posdigits, positions, total_digits = dissect(input().split())
    diff: int = 0
    for _ in range(min(nops, total_digits)):
        pos = positions[-1]
        digits = posdigits[pos]
        digit = digits.pop()
        diff += (9 - digit) * 10**pos
        if not digits:
            del posdigits[pos]
            positions.pop()
    print(diff)
