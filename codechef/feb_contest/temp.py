def my_lcs(x_string, y_string):
    matrix = [[0 for each_x in range(0, len(y_string) + 1)] for each_y in range(0, len(x_string) + 1)]
    for each_y in range(len(y_string)):
        for each_x in range(len(x_string)):
            prev_x = each_x - 1
            prev_y = each_y - 1
            if (x_string[prev_x] == y_string[prev_y]):
                matrix[each_x][each_y] = matrix[prev_x][prev_y] + 1
            else:
                matrix[each_x][each_y] = max(matrix[prev_x][each_y], matrix[each_x][prev_y])
    return matrix


# print /backtrack
def print_lcs(mtrx, x_string, y_string):
    result = []
    x, y = len(x_string), len(y_string)
    while x > 0 and y > 0:
        if x_string[x - 1] == y_string[y - 1]:
            result.append(x_string[x - 1])
            x -= 1
            y -= 1
        elif mtrx[x][y - 1] >= mtrx[x - 1][y]:
            y -= 1
        else:
            x -= 1

    return ''.join(result[::-1])


# inputa, inputb = "1ab", "2ab"  # ab
inputa, inputb="AAACCGTGAGTTATTCGTTCTAGAA", "CACCCCTAAGGTACCTTTGGTTC" #ACCTAGTACTTTG
# inputa, inputb="houseboat", "computer"#oue
# inputa, inputb="2193588", "21943588" #2193588
# inputa, inputb="ABCBDAB", "BDCABA" #BDAB
result = my_lcs(inputa, inputb)

print(inputa)
print(inputb)
print(print_lcs(result, inputa, inputb))
