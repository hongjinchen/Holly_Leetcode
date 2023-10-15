# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # nums=[i**2 for i in nums]
        # nums.sort()
        # return nums
        # 双指针法!
        start=0
        end=len(nums)-1
        result=[]

        while start<=end:
            if abs(nums[start])>abs(nums[end]):
                result.append(nums[start]**2)
                start+=1
            else:
                result.append(nums[end]**2)
                end-=1
        result.reverse()
        return result


if __name__=="__main__":
    solution=Solution()
    nums=[-4,-1,0,3,10]
    print(solution.sortedSquares(nums))