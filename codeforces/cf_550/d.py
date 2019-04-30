from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))


def get_next_idx(idx, array, max_elem):
    n = len(array)
    done = False
    while idx < n and not done:
        if array[idx] == max_elem:
            idx += 1
        else:
            done = True

    return idx


def get_next_chunk(start_idx, array, max_elem):
    chunk = list()
    n = len(array)
    done = False

    while start_idx < n and not done:
        if array[start_idx] != max_elem:
            chunk.append((array[start_idx], start_idx))
            start_idx += 1
        else:
            done = True

    return start_idx, chunk


def get_operations(chunk, type, max_elem):
    operations = list()
    if type == 'left':
        for chunk_elem in chunk:
            curr_elem = chunk_elem[0]
            curr_idx = chunk_elem[1]

            if curr_elem < max_elem:
                op_type = 1
            else:
                op_type = 2

            operation = (op_type, curr_idx + 1, curr_idx - 1 + 1)
            operations.append(operation)
    else:
        for chunk_elem in chunk[::-1]:
            curr_elem = chunk_elem[0]
            curr_idx = chunk_elem[1]

            if curr_elem < max_elem:
                op_type = 1
            else:
                op_type = 2

            operation = (op_type, curr_idx+1, curr_idx + 1 + 1)
            operations.append(operation)

    return operations

elem_counts = dict()
max_count = 0
max_elem = -1
for ai in a:
    if ai in elem_counts:
        elem_counts[ai] += 1
    else:
        elem_counts[ai] = 1

    if elem_counts[ai] > max_count:
        max_count = elem_counts[ai]
        max_elem = ai


num_ops = 0
ops = list()


# print(max_elem)

if len(elem_counts) == 1:
    print(0)
else:
    idx = get_next_idx(0, a, max_elem)
    # print(idx)
    all_operations = list()
    if idx == 0:
        idx, curr_chunk = get_next_chunk(idx, a, max_elem)
        # print(idx, curr_chunk)
        operations = get_operations(curr_chunk, 'right', max_elem)
        all_operations.extend(operations)


    while idx < n:
        idx = get_next_idx(idx, a, max_elem)
        idx, curr_chunk = get_next_chunk(idx, a, max_elem)
        # print(idx, curr_chunk)
        operations = get_operations(curr_chunk, 'left', max_elem)
        all_operations.extend(operations)

    print(len(all_operations))
    # print(all_operations)
    for operation in all_operations:
        # print(operation)
        print(" ".join([str(x) for x in operation]))

