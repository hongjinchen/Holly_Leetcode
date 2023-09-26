# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        
        answer = x
        # 正
        if n > 0:
            n = n-1
            while n != 0:
                answer = answer*x
                n = n-1
        # 负
        if n < 0:
            n = n-1
            while n != 0:
                answer = answer/x
                n = n+1
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.00000, -2))
