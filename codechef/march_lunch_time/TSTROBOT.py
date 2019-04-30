for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    s = input()

    points = [x]
    for dir in s:
        if dir == 'L':
            x -= 1
            points.append(x)
        else:
            x += 1
            points.append(x)

    print(len(set(points)))