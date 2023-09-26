# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# matrix = [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # 存在两个轴，m和n轴，m轴是行，n轴是列
        # 将当前遍历所在的位置看做是一个优先增加的运动。
        # 并且优先修改n轴
        # 首先，如果len(matrix[0])>location_n,那么增加location_n，不修改location_m,而如果len(matrix[0])=location_n，开始修改location_m
        # 这意味着增加location_m,不修改location_n，直到location_m=len(matrix)-1，再进行n轴方向的运动
        # 并且在遍历过程中，将经过的数据都删除为None，这样就可以避免重复遍历
        # 最终的终点为(m/2+1,n/2+1)-如果m和n都是奇数

        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [matrix[i][0] for i in range(len(matrix))]

        location_m = 0
        location_n = 0

        end_m = 0
        end_n = 0

        # 终止位置不是中点,
        if len(matrix) % 2 != 0:
            end_m = len(matrix) // 2
            number = len(matrix) // 2
            end_n = len(matrix[0]) - number-1
        else:
            end_m = len(matrix) // 2
            number = len(matrix) // 2
            end_n = 0 + number-1

        largest_m = len(matrix)-1
        largest_n = len(matrix[0])-1
        answer_list = [matrix[0][0]]
        while location_m != end_m or location_n != end_n:
            while largest_n > location_n:
                location_n = location_n+1
                answer_list.append(matrix[location_m][location_n])
            if location_m == end_m and location_n == end_n:
                break
            largest_n = largest_n-1

            while largest_m > location_m:
                location_m = location_m+1
                answer_list.append(matrix[location_m][location_n])
            if location_m == end_m and location_n == end_n:
                break
            largest_m = largest_m-1

            while location_n > 0:
                location_n = location_n-1
                answer_list.append(matrix[location_m][location_n])
            if location_m == end_m and location_n == end_n:
                break

            while location_m > largest_m and location_m > 0:
                location_m = location_m-1
                answer_list.append(matrix[location_m][location_n])
            if location_m == end_m and location_n == end_n:
                break
            
        return answer_list


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
