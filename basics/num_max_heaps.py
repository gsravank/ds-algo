import math


def get_num_children(n):


    h = int((math.log(n, 2)))
    if h == 0:
        nl = 0
    else:
        lr = n - int(math.pow(2, h) - 1)
        max_lr = int(math.pow(2, h))

        if lr >= int(max_lr / 2):
            nl = int(math.pow(2, h) - 1)
        else:
            nl = int(math.pow(2, h - 1)) - 1 + lr

    return nl

n = 5
nl = get_num_children(n)
nr = n - 1 - nl

print(n)
print('\n\n')
print(1)
print(nl, nr)