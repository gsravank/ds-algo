for _ in range(int(input())):
    n, d = input().strip().split()
    d = int(d)

    # n, d = list(map(int, input().strip().split()))

    digits = list()
    for ch in n:
        digits.append(int(ch))
    digits = digits[::-1]
    # while n != 0:
    #     digits.append(n % 10)
    #     n = int(n / 10)
    num_digits = len(digits)
    # print("Reversed digits")
    # print(digits)

    min_till = list()
    curr_min = 10
    for dig in digits:
        if dig <= curr_min:
            curr_min = dig
            if curr_min <= d:
                min_till.append(curr_min)
    # print("Minimum till:")
    # print(min_till)
    num_remaining_digits = num_digits - len(min_till)

    final_digits = ([d] * num_remaining_digits) + min_till
    # print("Final digits")
    # print(final_digits)

    final_num = 0
    for idx, elem in enumerate(final_digits[::-1]):
        final_num *= 10
        final_num += elem
    # print("Final number")
    print(final_num)
