
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # if len(nums)==0:
        #     return True 
        # n = len(nums)
        # def dfs(index):
        #     if index>=n-1:
        #         return True
        #     for i in range(1,nums[index]+1):
        #         if dfs(i+index):
        #             return True
        #     return False
        # return dfs(0)

        # if len(nums)==1:
        #     return True
        # if len(nums)==0:
        #     return True
        # for i in range(1,nums[0]+1):
        #     if self.canJump(nums[i:]):
        #         return True
        # return False
        # 两种递归的方法都超出时间的限制，但应该都work
        n = len(nums)

        state=[False]*n
        state[0]=True
        for i in range(1,n):
            for j in range(i):
                if state[j] and nums[j]+j>=i:
                    # 证明nums[j]+j>=i 从j点可以到i点，state[j]证明可以到j点
                    state[i]=True
        return state[n-1]

if __name__ == "__main__":
    solution=Solution()
    nums = [2,3,1,1,4]
    print(solution.canJump(nums))    
