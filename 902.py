# digits = ["3","4","5","6"]
# digits=sorted(digits)
# n = 64
# n = str(n)
# totalNumber = 0
# subNumber = 0
# number=0
# if len(n) == 1:
#     smallerNumber = 0
#     for item in digits:
#         if int(item) <= int(n):
#             smallerNumber = smallerNumber + 1
#     print(smallerNumber)
# #确认n的位数，得到所有少于该位数的组合，例如n的长度为4，所有长度为3的组合都小于该数
# if len(n) - 1 > 0:
#     for index in range(len(n) - 1):
#         totalNumber = totalNumber + len(digits)**(index + 1)
# else:
#     totalNumber = 0
# # 从第一位开始确认，数组中是否有小于该位数的数字，如果有则获得总体的数字的数量，如果没有就为1,
# # 然后每位数上获得的数字相乘，最后的数字为大于len(str(n)) - 1位数的可以组合的方式
# if int(n) % 10 > 0:
#     subNumber=1
#     additional=0
#     while len(n) > 1:
#         compareNumber = n[1]
#         compareNumber = int(compareNumber)
#         smallerNumber = 0
#         for item in digits:
#             if int(item) < compareNumber:
#                 smallerNumber = smallerNumber + 1
#             if int(item) == compareNumber:
#                 n = n[1:]
#                 additional=1
#                 continue
#             additional=additional*(smallerNumber+additional)

#         subNumber = subNumber * smallerNumber*len(digits)
#         n = n[1:]

# print("subNumber",subNumber)
# print(subNumber + totalNumber)


def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
    digits = set(digits)
    digits = sorted([int(i) for i in digits])

    def bound(x):
        return len(digits)**x

    def bound_with_limit(k, x):
        if x == 1:
            return bisect_right(digits, int(k[0]))
        t = int(k[0])
        b = bisect_left(digits, t)
        flag = b * bound(x - 1)
        if b < len(digits) and digits[b] == t:
            flag += bound_with_limit(k[1:], x - 1)
        return flag

    n = str(n)
    a = bound_with_limit(n, len(n))
    for i in range(1, len(n)):
        a += bound(i)
    return a


# 作者：qian-li-ma-8
# 链接：https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/solution/jian-dan-di-gui-ji-ke-by-qian-li-ma-8-cjyw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。