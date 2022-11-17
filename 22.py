n = 4
List=[""]
while(n!=0):
    NewList=[]
    for item in List:
        string1=item+"()"
        string2="()"+item
        string3="("+item+")"
        NewList.append(string1)
        NewList.append(string2)
        NewList.append(string3)
    NewList=list(set(NewList))
    List=NewList
    n=n-1
print(len(List))
lista=["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
print(len(lista))
print(len(list(set(lista))))