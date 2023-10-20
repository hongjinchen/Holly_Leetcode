# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

# 不占用额外内存空间能否做到？

# 给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # new_matrix = matrix.copy()
        # new_matrix 和 matrix 是两个独立的列表对象，但它们内部的元素仍然是相同的引用，也就是说，它们共享相同的子列表。
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix_new[j][len(matrix)-1-i] = matrix[i][j]
        
        # matrix=matrix_new.copy()
        # 这是一种创建原始矩阵的一个新副本的方式，并将其指定给新的变量 matrix。这个新的变量 matrix 不再与原始矩阵共享内存，它指向一个完全独立的矩阵对象，其内容与 matrix_new 相同。这种方式不会修改原始矩阵，而是创建一个新的矩阵对象。
        # matrix[:] = matrix_new：原地修改
        # 这是一种原地修改原始矩阵的方式。它将 matrix_new 中的内容复制到 matrix 中，但不更改 matrix 变量本身的引用。这意味着原始的 matrix 变量仍然指向相同的内存地址，但其内容已经被更新为 matrix_new 的内容。这种方式不会创建新的矩阵对象，因此在内存使用上更高效。
        matrix[:] = matrix_new
if __name__=="__main__":
    s=Solution()
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))