# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
# 如果 needle 不是 haystack 的一部分，则返回  -1 。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        if len(needle)>len(haystack):
            return -1
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
if __name__=="__main__":
    s=Solution()
    print(s.strStr("hello","ll"))