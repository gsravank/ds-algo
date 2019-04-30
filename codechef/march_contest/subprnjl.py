import math
from collections import Counter
import bisect


def count(arr, x, n):
    # get the index of first occurrence of x
    i = first(arr, 0, n - 1, x)

    # If x doesn't exist then return -1
    if i == -1:
        return i

    # Else get the index of last occurrence of x
    j = last(arr, i, n - 1, x)

    # return count
    return j - i + 1


def first(arr, low, high, x):
    if high >= low:
        # low + (high - low)/2
        mid = (low + high) // 2

        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x)
        else:
            return first(arr, low, (mid - 1), x)
    return -1


def last(arr, low, high, x):
    if high >= low:
        # low + (high - low)/2
        mid = (low + high) // 2

        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid - 1), x)
        else:
            return last(arr, (mid + 1), high, x)

    return -1


def get_idx(k, p):
    mult = int(math.ceil(float(k) / p))
    idx = int(math.ceil(float(k) / mult)) - 1
    return idx


def get_beauty_count(array, p, k, n):
    ans = 0

    ip = get_idx(k, p)
    # print("ip = {}".format(ip))
    s = array[:p]
    sS = sorted(s)

    elem = sS[ip]
    counts = Counter(s)

    count_elem = counts[elem]

    if count_elem in counts and counts[count_elem] > 0:
        # print("Elem = {}, Count of that = {} and this count is present in {}".format(elem, count_elem, sS))
        ans += 1

    # print(sS)
    # print(counts)

    for next_end in range(p, n):
        # print('\n')
        # find and remove first elem from prev subarray
        del_idx = first(sS, 0, p - 1, array[next_end - p])
        sS.pop(del_idx)

        # add last elem from current subarray
        new_elem = array[next_end]
        bisect.insort(sS, new_elem)

        # change counts
        counts[array[next_end - p]] -= 1

        if new_elem in counts:
            counts[new_elem] += 1
        else:
            counts[new_elem] = 1

        elem = sS[ip]
        count_elem = counts[elem]

        if count_elem in counts and counts[count_elem] > 0:
            # print("Elem = {}, Count of that = {} and this count is present in {}".format(elem, count_elem, sS))
            ans += 1

        # print(sS)
        # print(counts)

    # print("\nNumber of beautiful subarrays of size {} = {}".format(p, ans))
    return ans


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    beauty_count = 0
    for subarray_size in range(1, n+1):
        # print('Subarray size: {}'.format(subarray_size))
        beauty_count += get_beauty_count(a, subarray_size, k, n)
        # print('\n\n=====================================\n\n')

    print(beauty_count)

"""
2
5 3
1 2 3 4 5
10 4
7 3 3 4 5 8 2 1 9 1

"""
