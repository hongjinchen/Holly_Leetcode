class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = ""
        answer_number = 0
        if dividend == 0:
            return 0
        if divisor == 1:
            if dividend > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif dividend < -2 ** 31:
                return -2 ** 31
            return dividend

        if str(dividend)[0] == "-" and str(divisor)[0] != "-":
            answer = "-"
        elif str(dividend)[0] != "-" and str(divisor)[0] == "-":
            answer = "-"
        else:
            answer = "+"

        if divisor == -1:
            if dividend > 2 ** 31:
                return -2 ** 31
            elif dividend < -2 ** 31+1:
                return 2 ** 31 - 1
            return -dividend
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            answer_number += 1

        if answer == "+":
            answer_number = answer_number
        else:
            answer_number = -answer_number

        # 假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。本题中，如果商 严格大于 231 − 1 ，则返回 231 − 1 ；如果商 严格小于 -231 ，则返回 -231 。
        if answer_number > 2 ** 31 - 1:
            print("check")
            return 2 ** 31 - 1
        elif answer_number < -2 ** 31:
            return -2 ** 31
        return answer_number


if __name__ == "__main__":
    dividend = 2147483647
    divisor = 2
    new_solu = Solution()
    print(new_solu.divide(dividend, divisor))
