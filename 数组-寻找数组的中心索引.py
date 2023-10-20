# 给你一个整数数组 nums ，请计算数组的 中心下标 。

# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1

# 输入：nums = [1, 7, 3, 6, 5, 6]
# 输出：3
# 解释：
# 中心下标是 3 。
# 左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
# 右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 0
        left_sum = 0
        right_sum = sum(nums)

        index=0
        while index<=len(nums)-1:
            right_sum=right_sum-nums[index]
            if left_sum==right_sum:
                return index
            left_sum+=nums[index]
            index+=1
        return -1



if __name__=="__main__":
    s = Solution()
    print(s.pivotIndex([2,1,-1]))