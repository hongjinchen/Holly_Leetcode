def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for number in range(m + 1)]

# [[0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 1],
#  [0, 1, 1, 1, 1, 2],
#  [0, 1, 1, 2, 2, 2],
#  [0, 1, 1, 2, 2, 3],
#  [0, 1, 2, 2, 2, 3],
#  [0, 1, 2, 2, 3, 3],
#  [0, 1, 2, 2, 3, 4]]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[j-1] == s2[i-1]:
                dp[j][i] = dp[j-1][i-1]+1
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])

    # 获得最长公共子序列
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs


# 测试
s1 = "ABCBDAB"
s2 = "BDCAB"
print(longest_common_subsequence(s1, s2))
