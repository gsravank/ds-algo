def get_min_adjacent_distance(values):
    min_dist = values[1] - values[0]
    for i in range(1, len(values) - 1):
        min_dist = min(min_dist, values[i+1] - values[i])

    return min_dist


for _ in range(int(input())):
    n = int(input())
    points = list()
    for _ in range(n):
        points.append(list(map(int, input().strip().split())))

    x_plus_y = sorted([point[0] + point[1] for point in points])
    x_minus_y = sorted([point[0] - point[1] for point in points])

    min_plus = get_min_adjacent_distance(x_plus_y)
    min_minus = get_min_adjacent_distance(x_minus_y)

    overall_min = min(min_plus, min_minus) / 2
    print(overall_min)

"""
2
3
0 0
0 1
0 -1
3
0 1
1 0
-1 0

"""