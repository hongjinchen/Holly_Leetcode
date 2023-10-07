# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board:
            return False
        
        
        
        
if __name__ == "__main__":
    s = Solution()
    s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")