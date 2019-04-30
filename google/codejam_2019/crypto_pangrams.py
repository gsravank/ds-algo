# import math


def computeGCD(x, y):
    while y:
        x, y = y, x % y

    return int(x)


for ti in range(int(input())):
    N, L = list(map(int, input().strip().split()))
    cvals = list(map(int, input().strip().split()))

    primes = [0 for _ in range(L+1)]
    for idx in range(L-1):
        if cvals[idx] != cvals[idx + 1]:
            i0 = idx
            break

    primes[i0 + 1] = computeGCD(cvals[i0], cvals[i0 + 1])
    for idx in range(i0, -1, -1):
        primes[idx] = int(cvals[idx] / primes[idx + 1])
    for idx in range(i0+2, L+1):
        primes[idx] = int(cvals[idx - 1] / primes[idx - 1])

    # print(len(set(primes)))

    # print(primes)
    sorted_prime_idx = sorted([(p, idx) for idx, p in enumerate(primes)], key=lambda x: x[0], reverse=False)
    # print(sorted_prime_idx)

    idx_to_char_map = dict()
    curr_ord = 64
    prev_prime = None
    for p_idx in sorted_prime_idx:
        curr_prime = p_idx[0]
        curr_idx = p_idx[1]

        if curr_prime != prev_prime:
            curr_ord += 1

        idx_to_char_map[curr_idx] = chr(curr_ord)
        prev_prime = curr_prime
    # print(idx_to_char_map)
    # print(sorted(idx_to_char_map.keys()))
    orig_text = [idx_to_char_map[idx] for idx in range(L+1)]
    print("Case #{}: {}".format(ti + 1, ''.join(orig_text)))



"""
2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

"""