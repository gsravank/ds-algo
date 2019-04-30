def check_diverse(s):
    if len(s) == 1:
        return True

    if len(s) == len(set(s)):
        ords = [ord(ch) for ch in s]

        min_ords = min(ords)
        max_ords = max(ords)

        if max_ords - min_ords + 1 == len(s):
            return True
        else:
            return False
    else:
        return False


for _ in range(int(input())):
    s = input()

    if check_diverse(s):
        print("Yes")
    else:
        print("No")


"""
8
fced
xyz
r
dabcef
az
aa
bad
babc

"""