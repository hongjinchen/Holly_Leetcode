# @param score int整型一维数组 运动员成绩
# @return string字符串一维数组
#
class Solution:
    def findRelativeRanks(self , score ):
        
        if len(score)==0:
            return []
        if len(score)==1:
            return ["Gold Medal"]
        
        list=[]
        map={}
        for index in range(len(score)):
            num=int(score[index])
            list.append(num)
            map[num]=index
        
        list=sorted(list,reverse=True)
        
        answer=[0]*len(list)
        for index in range(len(list)):
            num=list[index]
            if index==0:
                answer[map[num]]="Gold Medal"
            elif index==1:
                answer[map[num]]="Silver Medal"
            elif index==2:
                answer[map[num]]="Bronze Medal"
            else:
                answer[map[num]]=str(index+1)
                
        return answer


if __name__=="__main__":
    solution=Solution()
    score=[5, 4, 3, 2, 1]
    print(solution.findRelativeRanks(score))
        # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
