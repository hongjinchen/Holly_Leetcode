# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

# 示例 1：

# 输入：nums = [1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        answer=0

        left=0
        right=0

        while right<len(nums):
            if nums[right]==1:
                right+=1
            else:
                answer=max(answer,right-left)
                right+=1
                left=right
        return max(answer,right-left)


if __name__=="__main__":
    s=Solution()
    print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))