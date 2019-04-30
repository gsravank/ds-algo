# list(map(int, input().strip().split()))

n, m = list(map(int, input().strip().split()))

if m % n != 0:
    print(-1)
else:
    rem = int(m / n)
    # print(rem)

    count = 0
    while rem % 2 == 0:
        rem = int(rem / 2)
        count += 1

    # print(rem)
    # print(count)

    while rem % 3 == 0:
        rem = int(rem / 3)
        count += 1

    if rem != 1:
        print(-1)
    else:
        print(count)