# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

# 问总共有多少条不同的路径？

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # 排列组合
        # # 从左上角到右下角，一共需要走m+n-2步，其中m-1步向下，n-1步向右
        # # C(m+n-2,m-1)
        # top = 1
        # for index in range(m+n-1-(m-1), m+n-1):
        #     top *= index
        # bottom = 1
        # for index in range(1, m):
        #     bottom *= index

        # return int(top/bottom)

        # # 递归--超时
        # if m == 1 or n == 1:
        #     return 1
        # # 向下或者向右
        # return self.uniquePaths(m-1, n)+self.uniquePaths(m, n-1)

        # 动态规划
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # f = [
        #     [1, 1, 1, 1],  # 第一行
        #     [1, 0, 0, 0],  # 第二行
        #     [1, 0, 0, 0]   # 第三行
        # ]
        for i in range(1, m):
            for j in range(1,n):
                f[i][j] = f[i-1][j]+f[i][j-1]
        
        return f[m-1][n-1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))
