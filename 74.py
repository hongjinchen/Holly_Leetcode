# 给你一个满足下述两条属性的 m x n 整数矩阵：

# 每行中的整数从左到右按非递减顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: