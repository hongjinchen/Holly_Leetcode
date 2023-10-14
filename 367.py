# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

# 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。

# 不能使用任何内置的库函数，如  sqrt 。

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.binary(num,1,num)
    def binary(self,num,l,r):
        mid=(l+r)//2
        if l>r:
            return False
        
        if num<mid*mid:
            return self.binary(num,l,mid-1)
        elif num>mid*mid:
            return self.binary(num,mid+1,r)
        else:
            return True


if __name__=="__main__":
    num=16
    s=Solution()
    print(s.isPerfectSquare(num))