# 
# @param nums int整型一维数组 
# @return int整型
#

class Solution:
    def findUnsortedSubarray(self , nums ):
        
        if len(nums)==0 or len(nums)==1:
            return 0
        
        sorted_nums=sorted(nums)
        list=[True]*len(nums)
        in_order=True
        for index in range(len(nums)):
            if sorted_nums[index]!=nums[index]:
                list[index]=False
                in_order=False
        
        if in_order:
            return 0
        else:
            start=len(nums)
            end=-1
            
            for index in range(len(list)):
                if list[index]==False:
                    if start==len(nums):
                        # 选择最小的false所在的位置
                        start=index
                
                    if index>end:
                        end=index
            
            return end-start+1

if __name__=="__main__":
    solu=Solution()
    nums=[1,2,3,4]
    print(solu.findUnsortedSubarray(nums))