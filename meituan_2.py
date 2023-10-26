class Solution:
    def IsContinuous(self , numbers: list[int]) -> bool:
        # write code here
        numbers=sorted(numbers) 
    
        index=0
        min_num=-1
        while index!=len(numbers) or min_num!=-1:
#             最小数字
            print(numbers[index])
            if numbers[index]!=0:    
                min_num=numbers[index]
            index+=1
        pre_num=-1
        
        for index in range(min_num,len(numbers)):
            if pre_num==-1:
                pre_num=numbers[index]
            
            if numbers[index]!=pre_num:
                continue
            else:
                return False
        max_num=numbers[-1]
        number_need=max_num-min_num-1
        if number_need-(min_num+1)-(4-min_num)>0:
            return False
        elif number_need-(min_num+1)-(4-min_num)<=0:
            return True


if __name__=="__main__":
    solution=Solution()
    numbers=[6,0,2,0,4]
    res=solution.IsContinuous(numbers)
    print(res)
