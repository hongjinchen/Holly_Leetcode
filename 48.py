# class Solution:
#     def rotate(self, matrix: list[list[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         需要直接修改输入的二维矩阵
#         """

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
length = len(matrix)
for index in range(length):
    for number in range(length):
        matrix[index].append(0)

for row in range(length):
    list=matrix[row]
    for index in range(length):
        matrix[index][length +row]=list[index]

for index in range(length):
    matrix[index]=matrix[index][length:]
    matrix[index]=matrix[index][: :-1]
print(matrix)
