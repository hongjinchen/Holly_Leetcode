# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 新的0和原有的0区分开！
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    matrix[i][j]='x'
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='x':
                    for n in range(len(matrix)):
                        if matrix[n][j]!='x':
                            matrix[n][j]=0
                        else:
                            continue
                    for m in range(len(matrix[i])):
                        if matrix[i][m]!='x':
                            matrix[i][m]=0
                        else:
                            continue
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='x':
                    matrix[i][j]=0
        print(matrix)
if __name__ == "__main__":
    s = Solution()
    print(s.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]))
