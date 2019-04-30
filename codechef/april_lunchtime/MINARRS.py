for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))

    # bin_strings = ['{0:030b}'.format(ai) for ai in a]
    # # print(bin_strings)
    #
    # x_digits = [[0, 0] for _ in range(30)]
    # for bin_string in bin_strings:
    #     for dig_num in range(30):
    #         if bin_string[dig_num] == '0':
    #             x_digits[dig_num][0] += 1
    #         else:
    #             x_digits[dig_num][1] += 1
    #
    # # print(x_digits)
    # x = 0
    # for i in range(30):
    #     x = (2 * x) + min(x_digits[i][0], x_digits[i][1])

    done = False
    x = 0
    dig = 0
    while not done:
        num_ones = 0
        for i in range(n):
            if a[i] % 2 == 1:
                num_ones += 1
            a[i] = int(a[i] / 2)

        if num_ones < n - num_ones:
            x += (num_ones * (2 ** dig))
        else:
            x += ( (n - num_ones) * (2 ** dig))

        dig += 1
        if all([ai == 0 for ai in a]):
            done = True

    print(x)


"""
3
5
2 3 4 5 6
4
7 7 7 7
3
1 1 3

"""