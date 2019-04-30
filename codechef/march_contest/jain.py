from itertools import chain, combinations
import time
from sys import stdin, stdout


all_chars = set(['a', 'e', 'i', 'o', 'u'])


def powerset(xs):
    ss = list(chain.from_iterable(combinations(xs, n) for n in range(1, len(xs) + 1)))
    final_ss = list()

    for elem in ss:
        # final_ss.append(''.join(sorted(list(elem))))
        final_ss.append(''.join(list(elem)))

    return final_ss


def get_non_dish(dish_chars):
    dish_chars = set(dish_chars)
    return ''.join(sorted(list(all_chars - dish_chars)))


for _ in range(int(input())):
    n = int(input())
    d = list()

    t1 = time.time()
    for _ in range(n):
        di = input()
        d.append(di)
    t2 = time.time()

    t3 = time.time()
    for i in range(n):
        d[i] = sorted(list(set(d[i])))
    t4 = time.time()
    # print(d)

    t5 = time.time()
    sub_strings = list()
    for i in range(n):
        sub_strings.append(powerset(d[i]))
    t6 = time.time()
    # print(sub_strings)

    t7 = time.time()
    occ_map = dict()
    for idx in range(n):
        for ss in sub_strings[idx]:
            if ss in occ_map:
                occ_map[ss] += 1
            else:
                occ_map[ss] = 1
    t8 = time.time()
    # print(occ_map)

    t9 = time.time()
    num_pairs = 0
    for dish in d:
        non_dish = get_non_dish(dish)
        if len(non_dish):
            if non_dish in occ_map:
                temp = occ_map[non_dish]
            else:
                temp = 0
        else:
            temp = n - 1
        num_pairs += temp
        # print('{} needs {}: Number of strings = {}'.format(dish, non_dish, temp))
    t10 = time.time()
    print(int(num_pairs / 2))

    print(t2-t1)
    print(t4-t3)
    print(t6-t5)
    print(t8-t7)
    print(t10-t9)

"""
2
3
aaeeii
aaiioouu
uuiioouu
5
aeio
aeiu
aeou
aiou
eiou

"""
