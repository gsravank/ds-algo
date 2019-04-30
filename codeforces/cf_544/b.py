
n, k = list(map(int, input().strip().split()))
d = list(map(int, input().strip().split()))

mod_dict = dict()
for di in d:
    di_mod = di % k

    if di_mod in mod_dict:
        mod_dict[di_mod] += 1
    else:
        mod_dict[di_mod] = 1

# print(mod_dict)

tot_boxes = 0
for i in range(1, k):
    if i in mod_dict and (k-i) in mod_dict:
        if i == k - i:
            tot_boxes += ( int(mod_dict[i] / 2) * 2 )
        else:
            tot_boxes += min(mod_dict[i], mod_dict[k-i])

if 0 in mod_dict:
    tot_boxes += ( int(mod_dict[0] / 2) * 2 )

print(tot_boxes)


# a = 10**14
# print(a)
# print(a - 1)