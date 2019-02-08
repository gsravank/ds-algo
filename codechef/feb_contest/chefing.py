t = int(input())

for _ in range(t):
    n = int(input())

    first = input()
    old_map = dict()
    for ch in first:
        old_map[ch] = True

    done = False
    for _ in range(n-1):
        new = input()
        if not done:
            new_map = dict()
            for char in new:
                if char in old_map:
                    new_map[char] = True

            old_map = new_map
            if len(old_map) == 0:
                done = True

    print(len(old_map))
