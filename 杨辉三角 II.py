# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

# 输入: rowIndex = 3
# 输出: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        res=[[1],[1,1]]
        for i in range(2,rowIndex+1):
            tmp=[1]
            for j in range(1,i):
                tmp.append(res[i-1][j-1]+res[i-1][j])
            tmp.append(1)
            res.append(tmp)
        return res[-1]


if __name__ == "__main__":
    solution=Solution()
    print(solution.getRow(3))