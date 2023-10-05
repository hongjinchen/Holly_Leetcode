# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

# 网格中的障碍物和空位置分别用 1 和 0 来表示。

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        if obstacleGrid[0][0]==1:
            return 0
        
        for list in obstacleGrid:
            for index in range(len(list)):
                item=list[index]
                if item==1:
                    list[index]=-1

        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i]==-1:
                obstacleGrid[0][i]=0
                break
            else:
                obstacleGrid[0][i]=1

        for j in range(len(obstacleGrid)):
            if obstacleGrid[j][0]==-1:
                obstacleGrid[j][0]=0
                break
            else:
                obstacleGrid[j][0]=1

        # 动态规划
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[i])):
                if obstacleGrid[i][j]==-1:
                    continue
                elif obstacleGrid[i-1][j]==-1:
                    obstacleGrid[i][j]=obstacleGrid[i][j-1]
                elif obstacleGrid[i][j-1]==-1:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        
        if obstacleGrid[-1][-1]==-1:
            return 0
        else:
            return obstacleGrid[-1][-1]



if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))