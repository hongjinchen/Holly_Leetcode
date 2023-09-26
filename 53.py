# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组 是数组中的一个连续部分。

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        if len(nums) == 1 or 0:
            return sum(nums)

        # subarray = [nums[0]]
        max_sum = nums[0]
        last_max_sum = nums[0]
        # DP:分解问题，以nums[i]结尾的最大子数组和
        for i in range(1, len(nums)):
            # 如果在上一个最大子数组和的基础上加上nums[i]，比原先的last_max_sum大，那么考虑添加nums[i]
            current_sum = nums[i] + last_max_sum
            if current_sum > max_sum:
                max_sum = current_sum
                last_max_sum = max_sum

            # 如果 在上一个最大子数组和的基础上加上nums[i]，比之前的last_max_sum小，那么更新last_max_sum并且不更新max_sum
            else:
                last_max_sum = current_sum

            # 如果nums[i]的值比last_max_sum大，那么nums[i]就是新的最大子数组和的起点，不考虑之前的内容
            if nums[i] >= last_max_sum:
                last_max_sum = nums[i]
            if nums[i] > max_sum:
                max_sum = nums[i]

        return max_sum


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([8, -19, 5, -4, 20]))
