n, k, A, B = list(map(int, input().split()))
a = list(map(int, input().split()))


start_position_map = dict()
end_position_map = dict()


def left_binary_search(item, elems):
    low = 0
    high = len(elems) - 1
    result = len(elems)

    while low <= high:
        mid = int((low + high) / 2)

        if elems[mid] > item:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


def right_binary_search(item, elems):
    low = 0
    high = len(elems) - 1
    result = -1

    while low <= high:
        mid = int((low + high) / 2)

        if elems[mid] <= item:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


def num_avengers(start, end, positions):
    if start in start_position_map:
        start_idx = start_position_map[start]
    else:
        start_idx = left_binary_search(start, positions)
        start_position_map[start] = start_idx

    if end in start_position_map:
        end_idx = start_position_map[end]
    else:
        end_idx = left_binary_search(end, positions)
        start_position_map[end] = end_idx

    # print('start_idx: {}, end_idx: {}'.format(start_idx, end_idx))
    if start_idx >= len(positions):
        return 0
    else:
        return end_idx - start_idx


def cost(start, end, positions, A, B):
    # print(start_position_map)
    # print(end_position_map)
    # print(start, end)
    num_aven = num_avengers(start, end, positions)
    # print(num_aven)
    # print('\n')
    if num_aven == 0:
        return A
    else:
        sing_cost = B * num_aven * (end - start)

        if end == start + 1:
            return sing_cost
        else:
            mid = start + int( (end - start) / 2 )
            left_cost = cost(start, mid, positions, A, B)
            right_cost = cost(mid, end, positions, A, B)

            return min(sing_cost, left_cost + right_cost)


sorted_a = sorted(a)
print(cost(0, 2**n, sorted_a, A, B))