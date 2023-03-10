#!/usr/bin/enb python3
"""
Ваня принес на кухню рулет, который он хочет разделить с коллегами.
Для этого он хочет разрезать рулет на N равных частей.
Разумеется, рулет можно резать только поперек.
Соотвественно, Костя сделает N - 1 разрез ножом через равные промежутки.

По возвращению с кофе-брейка Ваня задумался — а можно ли было обойтись меньшим числом движений,
будь нож Вани бесконечно длинным (иначе говоря, если он мог бы сделать сколько угодно разрезов за раз,
если эти разрезы лежат на одной прямой)?
Считается, что места для разрезов намечены заранее, и все разрезы делаются с ювелирной точностью.

Оказывается, что можно.
Например, если Ваня хотел бы разделить рулет на 4 части,
он мог бы обойтись двумя разрезами — сначала он разделил бы рулет на две половинки,
а потом совместил бы две половинки и разрезал обе пополам одновременно.

Вам дано число N, требуется сказать, каким минимальным числом разрезов можно обойтись.

Input
-----
N (1 <= N <= 2e9) - количество людей на кофе-брейке.

Output
------
Минимальное число движений, которое придется сделать Косте.

Limitations
-----------
* time - 1 s.
* memory - 256 MB.

Examples
--------
Ex. 1:
* Input: 6
* Output: 3

Ex. 2:
* Input: 5
* Output: 3

Notes
-----
Чтобы разрезать рулет на 6 частей,
Ване сначала придется разрезать его на две равные части,
после чего совместить две половинки и сделать два разреза.

Чтобы разрезать рулет на 5 частей,
Ване понадобится разделить его в соотношении 2:3,
после чего совместить два рулета по левому краю
и разрезать бОльший рулет на одинарные кусочки — меньший тоже разделится на одинарные.
"""

from math import log2, ceil

if __name__ == "__main__":
    people = int(input())
    cuts = ceil(log2(people)) if people else 0
    print(cuts)
