# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 请必须使用时间复杂度为 O(log n) 的算法。
# 二分查找

# 输入: nums = [1,3,5,6], target = 5
# 输出: 2

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid=(l+r)//2
        while l<=r:
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            mid=(l+r)//2
        return mid+1

if __name__=="__main__":
    s = Solution()
    print(s.searchInsert([1],4))