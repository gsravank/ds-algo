for ti in range(int(input())):
    n = input()

    a1_chars = list()
    a2_chars = list()

    for char in n:
        if char == '4':
            a1_chars.append('2')
            a2_chars.append('2')
        else:
            a1_chars.append(char)
            a2_chars.append('0')

    a1 = int(''.join(a1_chars))
    a2 = int(''.join(a2_chars))

    print("Case #{}: {} {}".format(ti+1, a1, a2))

