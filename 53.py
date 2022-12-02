# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max=self.findMax(nums,0,-100000000)
        return max

    def findMax(self, nums: list[int],number,max:list[int]):
        if len(nums)==number:
            return max
        # base case

        if max[index]+nums[0]>max[index]:
            max[index]=max[index]+nums[0]
            return self.findMax(nums[0:],index,max)
        else:

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    new=Solution()
    Solution.maxSubArray(nums)