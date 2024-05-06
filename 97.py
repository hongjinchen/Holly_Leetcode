#给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 
# 子字符串

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 注意：a + b 意味着字符串 a 和 b 连接。

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 首先检查长度匹配
        if len(s1) + len(s2) != len(s3):
            return False

        # 使用动态规划数组，dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符能否形成 s3 的前 i+j 个字符
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        # 初始化边界情况
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # 填充 dp 表
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]
    
if __name__=="__main__":
    sol=Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    
    print(sol.isInterleave(s1,s2,s3))
        