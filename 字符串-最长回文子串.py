# 给你一个字符串 s，找到 s 中最长的回文子串。

# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s)<2:
        #     return s
        # def expand_around_center(left,right):
        #     while left>0 and right<len(s) and s[left]==s[right]:
        #         left-=1
        #         right+=1
        #     return left+1,right-1
        # longest_palindrome=""
        # longest=0
        # for i in range(len(s)):
        #     start,end=expand_around_center(i,i)
        #     if end-start+1>longest:
        #         longest_palindrome=s[start:end+1]
        #         longest=end-start+1
            
        #     start,end=expand_around_center(i,i+1)
        #     if end-start+1>longest:
        #         longest_palindrome=s[start:end+1]
        #         longest=end-start+1
        # return longest_palindrome

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # 回文子串的范围是 left+1 到 right-1
        
        if len(s) < 2:
            return s

        longest = ""
        for i in range(len(s)):
            # 奇数长度的回文子串
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
            
            # 偶数长度的回文子串
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2
        return longest            

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("cbbd"))
