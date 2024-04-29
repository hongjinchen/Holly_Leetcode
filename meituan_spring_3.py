number_list=[2, 3, 4, 5]

n = 4
k = 4

def count_merges(arr, k):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    # 初始化单个元素的情况
    for i in range(n):
        dp[i][i] = 1 if arr[i] >= k else 0

    # 填充dp数组
    for length in range(2, n+1):  # 子数组的长度
        for i in range(n - length + 1):
            j = i + length - 1
            for m in range(i, j):
                sum_value = sum(arr[i:m+1]) + sum(arr[m+1:j+1])
                if sum_value >= k:
                    dp[i][j] += dp[i][m] * dp[m+1][j]

    return dp[0][n-1]


print(count_merges(number_list,k))


    
    
