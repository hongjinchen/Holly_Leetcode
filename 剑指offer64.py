class Solution:
    def sumNums(self, n: int) -> int:
        if n==0:
            return 0
        else:
            answer=self.sumNums(n-1)+n
            return answer
# &&：有短路功能的意思，当其中一个为false的时候，则不再运算其他的表达式，结果为false，只要是true，就往下进行，也就是只要有false，则结果就为false。
# java中的&&的功能和 python中的and相同
# class Solution:
#     def sumNums(self, n: int) -> int:
#         return n and self.sumNums(n - 1) + n

if __name__ == "__main__":
    solution=Solution()
    print(solution.sumNums(3))