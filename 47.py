# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

       # 动态规划
        if len(nums) == 1 or 0:
            return [nums]
        # [1,2,3]
        # [1]-->1
        # [1,2]-->[2,1],[1,2]-->2
        # [1,2,3]-->[2,1]->[3,2,1],[2,3,1],[2,1,3]-->[1,2]->[3,1,2],[1,3,2],[1,2,3]
        #在当前答案的元素的左右插入新的元素，能够成为作为新的排列方式
        answer=[[nums[0]]]
        for index_num in range(1,len(nums)):
            number=nums[index_num]
            new_answer=[]
            for item in answer:
                current=item
                for i in range(len(current)+1):
                    new_permute=current.copy()
                    new_permute.insert(i,number)
                    new_answer.append(new_permute)
                
            for item in new_answer:
                answer.append(item)
        new_answer=[]
        for item in answer:
            if len(item)==len(nums) and item not in new_answer:
                new_answer.append(item)
                
        return new_answer
                

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 3]))