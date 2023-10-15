# 给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其总和大于等于 target 的长度最小的
# 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # 滑动窗口
        start=0
        end=0
        if sum(nums)<target:
            return 0
        
        min_len = float('inf')  # 初始化为无穷大
        current_sum = 0  # 初始化当前子数组和为0

        while end < len(nums):
            current_sum += nums[end]  # 增加右端点的值
            end += 1  # 移动右端点

            # 当前子数组和大于等于target时，尝试缩小子数组长度
            while current_sum >= target:
                min_len = min(min_len, end - start)  # 更新最短长度
                current_sum -= nums[start]  # 减去左端点的值
                start += 1  # 移动左端点
                
        return min_len

if __name__=="__main__":
    solution=Solution()
    target=7
    nums=[2,3,1,2,4,3]
    print(solution.minSubArrayLen(target,nums))