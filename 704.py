# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.binary(nums,target,0,len(nums)-1)
        
    def binary(self,nums,target,l,r):

        if l>r:
            return -1
        
        mid=(l+r)//2

        if target>nums[mid]:
            return self.binary(nums,target,mid+1,r)
        elif target<nums[mid]:
            return self.binary(nums,target,l,mid-1)
        else:
            return mid

        



if __name__=="__main__":
    nums=[-1,0,3,5,9,12]
    target=9
    s=Solution()
    print(s.search(nums,target))