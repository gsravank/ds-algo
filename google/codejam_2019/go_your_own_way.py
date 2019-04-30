for ti in range(int(input())):
    n = int(input())
    lydia_path = input()
    my_path = list()

    for ch in lydia_path:
        if ch == 'S':
            my_path.append('E')
        else:
            my_path.append('S')

    print("Case #{}: {}".format(ti+1, ''.join(my_path)))