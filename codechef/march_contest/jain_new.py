from itertools import chain, combinations

all_chars = set(['a', 'e', 'i', 'o', 'u'])
powerset_map = dict()
non_dish_map = dict()


def powerset(xs):
    curr_str = ''.join(xs)
    if curr_str in powerset_map:
        return powerset_map[curr_str]

    ss = list(chain.from_iterable(combinations(xs, n) for n in range(1, len(xs) + 1)))
    final_ss = list()

    for elem in ss:
        final_ss.append(''.join(elem))

    powerset_map[curr_str] = final_ss
    return final_ss


def get_non_dish(dish_chars):
    temp = ''.join(dish_chars)
    if temp in non_dish_map:
        return non_dish_map[temp]

    dish_chars = set(dish_chars)
    ans = ''.join(sorted(list(all_chars - dish_chars)))
    non_dish_map[temp] = ans
    return ans


for _ in range(int(input())):
    n = int(input())
    d = list()

    occ_map = dict()

    for _ in range(n):
        dish = input()

        dish = sorted(list(set(dish)))
        d.append(dish)

    for idx, dish in enumerate(d):
        sub_strings = powerset(dish)

        for ss in sub_strings:
            if ss in occ_map:
                occ_map[ss] += 1
            else:
                occ_map[ss] = 1

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
    print(int(num_pairs / 2))


# print(powerset_map)
# print(non_dish_map)