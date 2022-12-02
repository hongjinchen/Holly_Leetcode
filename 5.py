# Longest Palindromic Substring
# 双指针
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer=s[0]
        if len(s)==1:
           return s 
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    res = s[i:j+1]
                    if res == res[::-1] and len(res) > len(answer):
                        answer=res
# -1表示最后一个元素，但是-1是结尾的index，
# 所以含义就是取原始数据的除最后一个元素之外的值 [::-1] 顺序相反操作
# [-1] 读取倒数第一个元素
        return answer
        
           

if __name__ == "__main__":
    s = "ac"
    new_solu=Solution()
    print(new_solu.longestPalindrome(s))
