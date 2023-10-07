# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # 动态规划
        
        answer = [[]]
        for i in nums:
            new_answer = []
            for j in answer:
                new_answer.append(j+[i])
            answer += new_answer

        return answer


if __name__ == "__main__":
    s = Solution()
    s.subsets([1, 2, 3])
