s = input()
t = input()

if len(s) != len(t):
    print('No')
else:
    i = 0
    found = False
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    while i < len(s) and not found:
        if s[i] in vowels:
            if t[i] in vowels:
                pass
            else:
                print('No')
                found = True
        else:
            if t[i] in vowels:
                print('No')
                found = True
            else:
                pass
        i += 1

    if not found:
        print('Yes')
