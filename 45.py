class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        # 使用贪心算法
        max_step,end,step=0,0,0
        for i in range(n-1):
            # if nums[i]>max_step:
            max_step=max(nums[i]+i,max_step)
            if i==end:
                end=max_step
                step=step+1
        return step
     # 每次在上次能跳到的范围（end）内选择一个能跳的最远的位置（也就是能跳到max_far位置的点）作为下次的起跳点


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    Solution=Solution()
    answer=Solution.jump(nums)
    print(answer)

# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 假设你总是可以到达数组的最后一个位置。

# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。