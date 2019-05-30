def get_layout(b):
    if b[0] == 0 or b[-1] == 0 or sum(b) != len(b):
        return None



    return


for ti in range(int(input())):
    b = list(map(int, input().strip().split()))

    rows = get_layout()

    if not rows:
        print("Case #{}: IMPOSSIBLE".format(ti + 1))
    else:
        print("Case #{}: {}".format(ti + 1, len(rows)))
        for row in rows:
            print(rows)

