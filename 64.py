# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # 动态规划
        # 每个位置的数值代表到达他的最小路径和，基数为本身的value
        # 初始化第一行和第一列
    
        for i in range(1,len(grid)):
            grid[i][0]+=grid[i-1][0]
        for j in range(1,len(grid[0])):
            grid[0][j]+=grid[0][j-1]
            
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]




if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))