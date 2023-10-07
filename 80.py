# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_one=-100000
        current_number=0
        index=0
        while index<=len(nums)-1:
            number=nums[index]
            if index==0:
                last_one=number
                current_number=1
                index+=1
            else:
                if last_one==number:
                    if current_number==2:
                        nums.pop(index)
                    else:
                        current_number+=1
                        index+=1
                else:
                    last_one=number
                    current_number=1
                    index+=1
        
        return len(nums)

        


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,1]))