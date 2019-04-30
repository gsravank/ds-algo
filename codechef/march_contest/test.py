import math


def get_idx(k, p):
    mult = int(math.ceil(float(k) / p))
    idx = int(math.ceil(float(k) / mult)) - 1
    return idx


k = 335
p = 3
for k in range(1, 20):
    print("k = {}, p = {}, idx = {}".format(k, p, get_idx(k, p)))

print("\n\n========================\n\n")
k = 50
for p in range(1, 70):
    print("k = {}, p = {}, idx = {}, p-idx = {}".format(k, p, get_idx(k, p), p-get_idx(k,p)))