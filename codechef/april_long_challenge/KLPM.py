def num_pairs_substrings_palindrome(s):
    n = len(s)

    pal_flag = [[0 for _ in range(n)] for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0

    # for i in range(n):
    #     pal_flag[i][i] = 1
    # for i in range(n-1):
    #     if s[i] == s[i+1]:
    #         pal_flag[i][i+1] = 1
    # for k in range(2, n):
    #     for i in range(0, n-k):
    #         j = i + k
    #         if s[i] == s[j] and pal_flag[i+1][j-1]:
    #             pal_flag[i][j] = 1

    for i in range(n):
        dp[i][i] = 0
        pal_flag[i][i] = 1

    for i in range(n-1):
        if s[i] == s[i+1]:
            pal_flag[i][i + 1] = 1
            dp[i][i+1] = 1
            answer += 1

    for k in range(2, n):
        for i in range(0, n-k):
            j = i + k
            if s[i] == s[j]:
                if pal_flag[i + 1][j - 1]:
                    pal_flag[i][j] = 1

                temp = 1
                temp += dp[i+1][j-1]

                for k1 in range(i+1, j):
                    temp += pal_flag[i+1][k1]
                    temp += pal_flag[k1][j-1]

                dp[i][j] = temp
                answer += temp

    # for row in pal_flag:
    #     print(row)
    # print('\n')
    # for row in dp:
    #     print(row)

    return answer


s = input()
print(num_pairs_substrings_palindrome(s))

"""
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
"""