# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # nums=sorted(nums)这会产生一个新的数组
        nums.sort()
        start=-1
        end=-1

        for index in range(len(nums)):
            if nums[index]==val:
                if start==-1:
                    start=index
                    end=index
                else:
                    end=index
        if start==-1:
            return len(nums)
        else:
            # nums=nums[:start]+nums[end+1:]
            # 这种方式会创建一个新的列表，其中包含了原列表中从头到 start 的元素和从 end 到最后的元素。然后，这个新列表会赋值给 nums。
            del nums[start:end+1]
            return len(nums)


if __name__=="__main__":
    solution=Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(solution.removeElement(nums,val))
    print(nums)