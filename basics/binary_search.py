def binary_search(items, elem):
    low = 0
    high = len(items) - 1
    
    while low <= high:
        mid = int((low + high) / 2)
        if items[mid] == elem:
            return mid
        elif items[mid] < elem:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 3, 6, 8, 12, 18, 25, 44, 47]
elems = [1, 12, 47, 0, 13, 50]

for elem in elems:
    print('Finding {} in the array..'.format(elem))
    print(binary_search(arr, elem))
    print('\n')