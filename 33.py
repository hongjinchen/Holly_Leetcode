# 整数数组 nums 按升序排列，数组中的值 互不相同 。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题(二分搜索?)。


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        
        # if target not in nums:
        #     return -1
        #in 运算的复杂度是O(n),所以不用in运算

        if target==nums[0]:
            return 0
        if target==nums[-1]:
            return len(nums)-1
        
        l, r = 0, len(nums) - 1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            
            if l == mid:
                l += 1
                continue

            if nums[mid]>nums[l]:
                #有序
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                #无序
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1



if __name__ == "__main__":
    new_solution=Solution()
    nums = [5,1,2,3,4]
    target = 1
    print(new_solution.search(nums,target))