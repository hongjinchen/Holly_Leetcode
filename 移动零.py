# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

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
        slow=0
        quick=0

        while quick<len(nums):
            if nums[quick]!=0:
                nums[slow]=nums[quick]
                quick+=1
                slow+=1
            else:
                quick+=1
        
        for i in range(slow,len(nums)):
            nums[i]=0

        return nums



if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes([0, 1, 0, 3, 12]))
    print(solution.moveZeroes([0]))