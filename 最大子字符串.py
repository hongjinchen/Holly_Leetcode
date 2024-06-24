# 两个字符串的最大公共子串（Longest Common Substring）是指两个字符串中相同字符的最大连续序列。

def longest_common_substring(str1, str2):
    len1, len2 = len(str1), len(str2)
    # 初始化dp数组
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    max_length = 0  # 最长公共子串的长度
    end_index = 0  # 最长公共子串在str1中的结束索引

    # 填充dp数组
    for i in range(1, len1 + 1):
        # 遍历str1的每个字符
        for j in range(1, len2 + 1):
            # 遍历str2的每个字符
            
            # str1 == str2当前字符相同，如果相同则在当前基础上+1 -- dp[i - 1][j - 1] 
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    # 根据end_index和max_length从dp数组中构造最长公共子串
    # 以str1的end_index作为标记点
    lcs = str1[end_index - max_length: end_index]
    return lcs

# 示例
str1 = "ABCDEF"
str2 = "DEFGHE"
print(longest_common_substring(str1, str2))  # 输出 "DEF"