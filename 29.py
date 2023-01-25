# 没做出来，暂时放弃了


# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         answer=0
#         dividend_abs=abs(dividend)
#         divisor_abs=abs(divisor)
#         neg=(dividend<0)!=(divisor<0)
#         temp=1
#         # 好厉害的方法 (dividend<0)是一个判断，(divisor<0)是另一个判断，
#         # 如果两个情况不相同就为负，就是neg为true
#         limit = 2**31 - 1

#         if divisor_abs==1:
#             answer=dividend_abs
#         else:
#             while dividend_abs >= abs(divisor):
#                 while dividend_abs > (divisor_abs << 1):
#                     divisor_abs <<= 1
#                     temp <<= 1
#                 dividend_abs -= divisor_abs
#                 divisor_abs = abs(divisor)
#                 answer += temp
#                 temp = 1
#         if neg:
#             answer=-answer

#         if -2**31 <= answer <= -2**31:
#             return answer
#         else:
            
#             return limit

        # 这里是在考虑超出integer极限的情况

if __name__ == "__main__":
    dividend = 10
    divisor = 3
    new_solu=Solution()
    print(new_solu.divide(dividend,divisor))