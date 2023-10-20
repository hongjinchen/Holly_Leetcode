# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             matrix[i][j] = "*"
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == "*":
        #             for m in range(len(matrix[i])):
        #                 item=matrix[i][m]
        #                 if item != "*":
        #                     matrix[i][m]=0
        #             for n in range(len(matrix)):
        #                 item=matrix[n][j]
        #                 if item != "*":
        #                     matrix[n][j] = 0

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == "*":
        #             matrix[i][j] = 0
        m,n=len(matrix),len(matrix[0])
        row=[0]*m
        col=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(m):
            for j in range(n):
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0

if __name__ == "__main__":
    s = Solution()
    print(s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
