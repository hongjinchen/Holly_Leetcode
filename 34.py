# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。(二分法)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==1:
            return [0,0] if nums[0]==target else [-1,-1]
        
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                l,r=mid,mid
                while l>0 and nums[l-1]==target:
                    l-=1
                while r<len(nums)-1 and nums[r+1]==target:
                    r+=1
                return [l,r]
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        return [-1,-1]


if __name__ == "__main__":
    new_solution=Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(new_solution.searchRange(nums,target))


