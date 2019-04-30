from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))

elem_map = defaultdict(lambda : list())
for ai in a:
    elem_map[ai].append(ai)

first = list()
second = list()
cannot = False

for key in elem_map:
    values = elem_map[key]

    if len(values) > 2:
        cannot = True
        break
    elif len(values) == 2:
        first.append(key)
        second.append(key)
    else:
        first.append(key)


if cannot:
    print("NO")
else:
    print("YES")
    first = sorted(first)
    second = sorted(second, reverse=True)

    print(len(first))
    print(" ".join([str(x) for x in first]))
    print(len(second))
    print(" ".join([str(x) for x in second]))
    # print('..')