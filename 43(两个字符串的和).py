# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #以num1为基准，从第一个字符开始逐步和num2相乘，并且根据当前字符所在的index推断该计算内容在answer中的位置，每一位在list中占一个位置，
        # 在最后返回之前将超过十位的部分移到前一个index中，由后往前逐位相加，第一个位置的进位不用考虑

        if num1=="0" or num2=="0":
            return "0"
        
        answer_list= [0] * (len(num1)+len(num2)-1)
        for num1_index in range(len(num1)):
            for num2_index in range(len(num2)):
                answer_list[num1_index+num2_index]=answer_list[num1_index+num2_index]+int(num1[num1_index])*int(num2[num2_index])
        
        left_value=0
        for index in range(len(answer_list)-1,-1,-1):
            if index!=0:
                current_value=answer_list[index]
                current_value=current_value+left_value
                if len(str(current_value))>1:
                    left_value=current_value//10
                    answer_list[index]=current_value%10
                else:
                    left_value=0
                    answer_list[index]=current_value
            elif index==0:
                answer_list[index]=answer_list[index]+left_value
        
        answer=""
        for number in answer_list:
            answer=answer+str(number)
        return answer


if "__main__" == __name__:
    New_solution = Solution()
    num1 = "18"
    num2 = "3"
    print (New_solution.multiply(num1, num2))