from fractions import Fraction

MOD = (10 ** 9) + 7
t = int(input())


def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

        # Make x positive
    if (x < 0):
        x = x + m0

    return x


def get_probability(n, k, m):
    print(n,k,m)
    if m == 1:
        print('One move left, so probability = {}/{}'.format(1,n))
        return Fraction(1, n)
    else:
        if n <= k:
            right_prob = Fraction(1, n)
            wrong_prob = Fraction(n-1, n)

            print('Prob of choosing correctly = {}/{}'.format(1, n))
            print('Prob of choosing wrongly = {}/{}'.format(n-1, n))

            if wrong_prob == 0:
                overall_prob = right_prob
                print('Overall probability = {}/{}'.format(overall_prob.numerator, overall_prob.denominator))
                return overall_prob
            else:
                overall_prob = right_prob + (wrong_prob * get_probability(n+k, k, m-1))
                print('Overall probability = {}/{}'.format(overall_prob.numerator, overall_prob.denominator))
                return overall_prob

        else:
            print('Remove {} boxes in this move..'.format(k))
            return get_probability(n % k, k, m-1)


def get_probability_iter(n, k, m):
    adds = list()
    mults = [Fraction(1)]

    while m > 0:
        if n <= k:
            right_prob = Fraction(1, n)
            wrong_prob = Fraction(n - 1, n)

            adds.append(right_prob)

            if m > 1:
                mults.append(wrong_prob)

            n = n + k
            m = m - 1
        else:
            if m == 1:
                right_prob = Fraction(1, n)

                adds.append(right_prob)

                m = m - 1
            else:
                n = n % k
                m = m - 1

    # mults.pop()
    # mults = [Fraction(1)] + mults
    # print(adds)
    # print(mults)

    final = Fraction(0)
    for idx in range(len(mults) - 1, -1, -1):
        # print(final)
        final += adds[idx]
        final *= mults[idx]
    # print(final)
    return final


for _ in range(t):
    n, k, m = list(map(int, input().strip().split()))

    # prob = get_probability(n, k, m)
    prob = get_probability_iter(n, k, m)

    p = prob.numerator
    q = prob.denominator
    print('\nAnswer = {}/{}'.format(p, q))
    print((p * mod_inverse(q, MOD)) % MOD)

"""
3
5 9 1
7 9 2
3 20 3

"""

