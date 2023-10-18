# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        min_length = min([len(str) for str in strs])
        if min_length==0:
            return ""
        ans=""
        for i in range(min_length):
            is_same = True
            for j in range(len(strs)):
                if strs[j][i]!=strs[0][i]:
                    is_same=False
            if is_same:
                ans+=strs[0][i]
            else:
                break
        return ans
                    

                    
            


if __name__=="__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
