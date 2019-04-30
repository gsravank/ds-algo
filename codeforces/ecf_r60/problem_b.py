n, m, k = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))

max = max(a)

max_count = 0
for elem in a:
    if elem == max:
        max_count += 1

    if max_count == 2:
        break


if max_count > 1:
    print(m * max)
else:
    max_but_one = -1
    for elem in a:
        if elem > max_but_one and elem < max:
            max_but_one = elem

    ans = int(m/(k+1)) * ((max * k) + max_but_one)
    ans += ( (m % (k+1)) * max)

    print(ans)
