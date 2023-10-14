# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

# 示例 1:

# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 示例 2:

# 输入: nums = [0]
# 输出: [0]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针法
        fast=0
        slow=0
        
        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
            else:
                fast+=1
        
        while slow<len(nums):
            nums[slow]=0
            slow+=1
        

                



if __name__=="__main__":
    solution=Solution()
    nums = [0,1,0,3,12]
    solution.moveZeroes(nums)
    print(nums)