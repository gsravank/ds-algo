import math


def get_sum(a, p, k):
    curr_den = 1
    curr_sum = 0

    sing_sums = ['-'] * p
    for elem in a[p:]:
        temp_sum = int(math.floor(float(elem) / curr_den))
        curr_sum += temp_sum
        curr_den += 1

        sing_sums.append(str(temp_sum))

        # if curr_sum > k:
        #     break
    # print(' '.join([str(x) for x in a]))
    print('\t'.join(sing_sums + [ '->', str(curr_sum)]))
    return curr_sum


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print('\n\n')

    for p in range(0, n+1):
        anger_sum = get_sum(a, p, k)
        # print("p = {}, anger sum = {}\n".format(p, anger_sum))

        if anger_sum <= k:
            print(p+1)
            break

"""
1
12 4
2 7 8 4 14 8 3 1 2 6 12 4 

"""