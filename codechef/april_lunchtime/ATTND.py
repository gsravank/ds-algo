from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    name_dict = defaultdict(lambda: 0)
    names = list()

    for ni in range(n):
        name = input().strip().lower()
        names.append(name)
        name_parts = name.split(' ')

        name_dict[name_parts[0]] += 1

    for name in names:
        first_name = name.split(' ')[0]

        if name_dict[first_name] > 1:
            print(name)
        else:
            print(first_name)



"""
1
4
hasan jaddouh
farhod khakimiyon
kerim kochekov
hasan khateeb

"""