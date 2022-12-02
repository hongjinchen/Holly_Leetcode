class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # res = []
        # def backtrack(candidates, path, target, start):
        #     if sum(path) == target:
        #         res.append(path[:])
        #         return
        #     if sum(path) > target:
        #         return
            
        #     for i in range(start,len(candidates)):
        #         path.append(candidates[i])
        #         backtrack(candidates, path, target, i)
        #         path.pop()
        # backtrack(candidates, [], target, 0)
        # return res
        
        # candidate里的值可以使用多次
        res, track = list(), list()
        def backtrack(nums, start,sum,target):
            # 基础情况
            if sum==target:
                res.append(track[:])
                print(track[:])
                return
            elif sum>target:
                return

            # 对于选择列表中的每个选择
            for i in range(start,len(nums)):
                track.append(nums[i])
                sum=sum+nums[i]
                # 递归
                backtrack(nums,i,sum,target)
                track.pop()
                sum=sum-nums[i]
        backtrack(candidates,0,0,target)
        return res

if __name__ == "__main__":
    solution=Solution()
    candidates = [2,3,6,7]
    target = 7
    print(solution.combinationSum(candidates,target))