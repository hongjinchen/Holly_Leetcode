from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits)==0:
            return([])
        numberList=list(digits)
        sort_list=[]
        for item in numberList:
            if item=="2":
                sort_list.append(["a","b","c"])
            elif item=="3":
                sort_list.append(["d","e","f"])
            elif item=="4":
                sort_list.append(["g","h","i"])            
            elif item=="5":
                sort_list.append(["j","k","l"])
            elif item=="6":
                sort_list.append(["m","n","o"])
            elif item=="7":
                sort_list.append(["p","q","r","s"])
            elif item=="8":
                sort_list.append(["t","u","v"])
            elif item=="9":
                sort_list.append(["w","x","y","z"])

        answer=sort_list[0]
        for index in range(1,len(sort_list)):
            new_list=[]
            for item in answer:
                for item2 in sort_list[index]:

                    new_list.append(item+item2)
            answer=new_list
        return answer
if __name__ == "__main__":
    digits= "2"
    solution=Solution()
    print(solution.letterCombinations(digits))