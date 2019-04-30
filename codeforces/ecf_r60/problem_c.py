import math


def get_step(direction):
    if direction == 'U':
        return 0, 1
    elif direction == 'D':
        return 0, -1
    elif direction == 'L':
        return -1, 0
    else:
        return 1, 0


def abs(x):
    return int(math.fabs(x))


def weather_cycle_end(s):
    start = [0, 0]
    for ch in s:
        step = get_step(ch)
        start = [start[i] + step[i] for i in range(2)]

    return start


def man_dist(x, y):
    return abs(x) + abs(y)


x1, y1 = list(map(int, input().strip().split()))
x2, y2 = list(map(int, input().strip().split()))
n = int(input())
s = input()

x_diff = x2 - x1
xdiff = x_diff
y_diff = y2 - y1
ydiff = y_diff
manh_dist = abs(x_diff) + abs(y_diff)


# min and last manhattan distance occurring in a cycle
# while moving closer to the destination
min_dist = man_dist(xdiff, ydiff)
min_steps = -1

for idx, ch in enumerate(s):
    step = get_step(ch)
    xdiff -= step[0]
    ydiff -= step[1]

    if xdiff == 0 and y_diff == 0:
        min_dist = 0
        min_steps = idx
    else:
        if abs(xdiff) > abs(ydiff):
            if xdiff > 0:
                my_step = [1, 0]
            else:
                my_step = [-1, 0]
        else:
            if ydiff > 0:
                my_step = [0, 1]
            else:
                my_step = [0, -1]

    xdiff += my_step[0]
    ydiff += my_step[1]
    curr_man_dist = man_dist(xdiff, ydiff)

    if curr_man_dist < min_dist:
        min_dist = curr_man_dist
        min_steps = idx

last_dist = man_dist(xdiff, ydiff)
dist_in_cycle = manh_dist - last_dist

if min_dist == 0:
    print(min_steps)
else:
    if dist_in_cycle <= 0:
        print(-1)
    else:
        num_cycles = int(manh_dist / dist_in_cycle)
        total_steps = num_cycles * n

        if manh_dist % dist_in_cycle == 0:
            print(total_steps)
        else:
            # what happens in the last cycle
            remaining_steps = 1