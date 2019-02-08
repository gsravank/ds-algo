def helper(string, l):
    # print(string)
    if string[-1] != ']':
        l.append(string)
        return l

    for i in range(len(string)):
        if string[i] == '[':
            break

    init_string = string[:i-1]
    mult = int(string[i-1])
    sub_str = string[i+1:-1]

    # print(init_string)
    # print(mult)
    # print(sub_str)
    # print('\n')

    l = helper(sub_str, l)
    l = l * mult
    l = [init_string] + l

    return l


def get_string(coded_string):
    final_list = list()
    final_list = helper(coded_string, final_list)
    # print(final_list)
    return ''.join(final_list)


cs = '3[xzb2[ca]]'
print(get_string(cs))