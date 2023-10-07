# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 必须在不使用库内置的 sort 函数的情况下解决这个问题。

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 冒泡排序
        for i in range(1, len(nums)):
            for j in range(0, len(nums)-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        

        

if __name__ == "__main__":
    s = Solution()
    nums = [2,0,2,1,1,0]
    print(s.sortColors(nums))
