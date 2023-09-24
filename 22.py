# n = 4
# List=[""]
# while(n!=0):
#     NewList=[]
#     for item in List:
#         string1=item+"()"
#         string2="()"+item
#         string3="("+item+")"
#         NewList.append(string1)
#         NewList.append(string2)
#         NewList.append(string3)
#     NewList=list(set(NewList))
#     List=NewList
#     n=n-1
# print(len(List))
# lista=["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# print(len(lista))
# print(len(list(set(lista))))
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answer_list=[]
        def DFS(left,right,answer):
            if left==0 and right==0:
                answer_list.append(answer)
                return
            if left>0:
                DFS(left-1,right,answer+"(")
            if right>left:
                DFS(left,right-1,answer+")")
        DFS(n,n,"")
        return answer_list
        



if __name__ == "__main__":
    divisor = 3
    new_solu=Solution()
    print(new_solu.generateParenthesis(divisor))