# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:
            return True
        for i in range(1,int(c**0.5)+1):
            rest=c-i**2
            if rest**0.5==int(rest**0.5):
                return True
        return False
            


if __name__=="__main__":
    solution=Solution()
    c = 5
    print(solution.judgeSquareSum(c))
