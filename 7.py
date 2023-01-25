class Solution:
    def reverse(self, x: int) -> int:
        answer=""
        x=str(x)
        if x[0]=="-":
            answer="-"
            x=x[1:]
        elif x[0]=="+":
            answer="+"
            x=x[1:]
        index=len(x)-1
        while index>=0:
            answer=answer+x[index]
            index=index-1
        answer=int(answer)
        if answer> (2**31-1) or answer<-2**31:
            return 0
        return int(answer)



if __name__ == "__main__":
    x = 123
    new_solu=Solution()
    print(new_solu.reverse(x))