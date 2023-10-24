# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

#  

# 示例 1：

# 输入：s = "Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s)==0:
            return ""
        elif len(s)==1:
            return s
        s_list=s.split(" ")
        answer=""
        for item in s_list:
            new_one=""
            new_one=item[::-1]
            answer+=new_one+" "
        
        return answer[:-1]



if __name__ == "__main__":
    solution=Solution()
    print(solution.reverseWords("Let's take LeetCode contest"))