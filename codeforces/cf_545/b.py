n = int(input())
c = input()
a = input()

only_acro = list()
only_clown = list()
both = list()
none = list()

for idx, (ai, ci) in enumerate(zip(a, c)):
    if ai == '1' and ci == '1':
        both.append(idx + 1)
    elif ai == '1' and ci == '0':
        only_acro.append(idx + 1)
    elif ai == '0' and ci == '1':
        only_clown.append(idx + 1)
    else:
        none.append(idx + 1)


m1 = len(only_clown)
m2 = len(both)
m3 = len(only_acro)
m4 = len(none)

# print(only_clown)
# print(only_acro)
# print(both)
# print(none)

first_perf = list()
if m1 > n/2 or m3 > n/2:
    print(-1)
else:
    if m1 + m2 <= m3:
        k = m1 + m2
        first_perf.extend(only_clown)
        first_perf.extend(both)

        rem = int(n/2) - len(first_perf)

        if rem <= len(none):
            first_perf.extend(none[:rem])
        else:
            first_perf.extend(none)
            first_perf.extend(only_acro[:(int(n/2)-len(first_perf))])
    else:
        if m2 + m3 <= m1:
            k = m2 + m3
            first_perf.extend(only_clown[:k])

            rem = int(n/2) - k
            first_perf.extend(none[:rem])
        else:
            if m1 <= m3:
                k = m1

                first_perf.extend(only_clown)
            else:
                k = m3

                first_perf.extend(only_clown[:k])

            rem = int(n / 2) - len(first_perf)
            first_perf.extend(none[:rem])



print(' '.join([str(x) for x in first_perf]))