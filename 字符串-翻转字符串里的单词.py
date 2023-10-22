# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。

# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

# 输入：s = "the sky is blue"
# 输出："blue is sky the"

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s)==0 or len(s)==1:
            return s
        
        s_list=s.split(" ")
        new_s_list=[""]*len(s_list)
        for index in range(len(s_list)):
            word=s_list[index]
            # if word!='':
            #     word=word[::-1]
            new_s_list[len(s_list)-index-1]=word
        
        answer=""
        for word in new_s_list:
            if word!='':
                answer+=word+" "
        
        return answer[:-1]


if __name__=="__main__":
    s=Solution()
    print(s.reverseWords("the sky is blue"))