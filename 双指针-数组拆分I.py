# 给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。

# 返回该 最大总和 。

# 输入：nums = [1,4,3,2]
# 输出：4
# 解释：所有可能的分法（忽略元素顺序）为：
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# 所以最大总和为 4

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        answer_list=[]
        for i in range(0,len(nums),2):
            answer_list.append(nums[i])
        return sum(answer_list)


if __name__=="__main__":
    s=Solution()
    print(s.arrayPairSum([1,4,3,2]))