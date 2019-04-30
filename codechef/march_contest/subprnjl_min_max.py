import math
import heapq as hp


def get_idx(k, p):
    mult = int(math.ceil(float(k) / p))
    idx = int(math.ceil(float(k) / mult)) - 1
    return idx


def get_beauty_count(array, start_idx, k, n):
    beauty_count = 0

    min_heap = list()
    max_heap = list()

    hp.heapify(min_heap)
    hp.heapify(max_heap)

    # print(min_heap)
    # print(max_heap)

    counts = dict()

    # length of subarray starts from 1 and goes till n-start
    for p in range(1, n-start_idx+1):
        # print('Curr length of subarray p={}'.format(p))
        elem_to_add = array[start_idx + p - 1]
        # print('Elem to add: {}'.format(elem_to_add))

        if len(min_heap) == 0 or elem_to_add >= min_heap[0]:
            hp.heappush(min_heap, elem_to_add)
        else:
            hp.heappush(max_heap, -1 * elem_to_add)

        # print("Min heap after adding: {}".format(min_heap))
        # print("Max heap after adding: {}".format(max_heap))

        if elem_to_add in counts:
            counts[elem_to_add] += 1
        else:
            counts[elem_to_add] = 1

        ip = get_idx(k, p)
        num_elems_in_max = ip
        curr_elems_in_max = len(max_heap)

        # print("ip: {}".format(ip))
        # print("num_elems_in_max: {}".format(num_elems_in_max))
        # print("curr_elems_in_max: {}".format(curr_elems_in_max))

        if curr_elems_in_max < num_elems_in_max:
            # add elems from min heap into max heap
            num_elems_to_add = num_elems_in_max - curr_elems_in_max
            for _ in range(num_elems_to_add):
                # pop min elem from min heap
                # push that elem * -1 into max heap
                min_elem = hp.heappop(min_heap)
                hp.heappush(max_heap, -1 * min_elem)
        elif curr_elems_in_max > num_elems_in_max:
            # add elems from max heap into min heap
            num_elems_to_add = curr_elems_in_max - num_elems_in_max
            for _ in range(num_elems_to_add):
                # pop max elem from max heap
                # push that elem * -1 into min heap
                max_elem = hp.heappop(max_heap)
                hp.heappush(min_heap, max_elem * -1)
        else:
            # num elems are perfect in both min and max heap
            pass

        # print("Min heap after adjusting: {}".format(min_heap))
        # print("Max heap after adjusting: {}".format(max_heap))

        elem_at_ip = min_heap[0]
        count_of_elem = counts[elem_at_ip]
        # print('Elem at ip={} is {}'.format(ip, elem_at_ip))
        # print("count of {} = {}".format(elem_at_ip, count_of_elem))
        if count_of_elem in counts:
            # print("count present in subarray")
            beauty_count += 1
        # else:
        #     print('count not present in subarray')
        # print('\n')

    return beauty_count


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    # For each starting point, get subarrays starting at that index
    beauty_count = 0
    for start_idx in range(n):
        # print('Start Idx: {}'.format(start_idx))
        beauty_count += get_beauty_count(a, start_idx, k, n)
        # print('\n=====================================\n')

    print(beauty_count)
    # print('\n********************\nAnswer = {}\n*******************\n'.format(beauty_count))


"""
1
3 3
1 2 3

"""