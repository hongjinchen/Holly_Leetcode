# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。


# 示例 1:

# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        # 迭代
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        res=[[1],[1,1]]
        for i in range(2,numRows):
            tmp=[1]
            for j in range(1,i):
                tmp.append(res[i-1][j-1]+res[i-1][j])
            tmp.append(1)
            res.append(tmp)
        return res



if __name__ == "__main__":
    solution=Solution()
    print(solution.generate(5))