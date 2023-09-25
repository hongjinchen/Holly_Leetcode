# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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
            if len(item)==len(nums):
                new_answer.append(item)
        return new_answer
                

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
