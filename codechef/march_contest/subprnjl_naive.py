import math


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


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    beauty_count = 0
    for start in range(n):
        for end in range(start, n):
            # For each subarray
            sub_array = a[start: end + 1]
            p = end - start + 1

            # Get the required element
            sorted_sub_array = sorted(sub_array)

            mult = int(math.ceil(float(k) / p))
            idx = int(math.ceil(float(k) / mult)) - 1

            required_elem = sorted_sub_array[idx]

            # Count occurence of that element in the subarray
            elem_count = count(sorted_sub_array, required_elem, p)

            # Does count calculated above occur in the subarray?
            count_occurrence = first(sorted_sub_array, 0, p-1, elem_count)

            if count_occurrence != -1:
                # print(start, end)
                # print(sub_array)
                # print(sorted_sub_array)
                # print("k = {}, p = {}".format(k, p))
                # print("mult = {}".format(mult))
                # print("sorted sub array idx = {}".format(idx))
                # print("required elem = {}".format(required_elem))
                # print("elem count in subarray = {}".format(elem_count))
                # print("Occurence position in count in sorted subarray = {}".format(occ + 1))
                # print('\n\n')
                # print(mult)
                beauty_count += 1

    print(beauty_count)
