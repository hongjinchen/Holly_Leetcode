# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        answer.append([])
        return self.dp(nums, answer)

    def dp(self, nums, answer):
        if len(nums) == 0:
            return answer

        for index in range(len(answer)):
            item = answer[index]
            new_one = item+[nums[0]]
            if new_one not in answer:
                answer.append(new_one)
        return self.dp(nums[1:], answer)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2]
    answer = s.subsetsWithDup(nums)
    print(answer)
