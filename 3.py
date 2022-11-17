class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = 0
        lookup = set()
        left_number = 0
        max_length = 0
        if not s:return 0
        for index in range(len(s)):
            if s[index:index + 1] in lookup:
                lookup.remove(s[index:index + 1])
                left_number += 1
                string_length -= 1

            else:
                lookup.add(s[index:index + 1])
                string_length += 1
                
            if string_length > max_length:
                max_length = string_length
        return max_length
