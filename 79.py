# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        return self.is_exist(0,0,board,word,0)
        
    def is_exist(self, x_index,y_index,board,word,k):
        if len(word)-1==k:
            return True
        
        if word[0]==board[x_index][y_index]:
            if x_index+1<=len(board)-1:
                return self.is_exist(x_index+1,y_index,board,word,k+1)
            if y_index+1<=len(board[0])-1:
                return self.is_exist(x_index,y_index+1,board,word,k+1)
        else:
            if x_index==len(board)-1 and y_index==len(board[0])-1:
                return False
            return self.is_exist(x_index,y_index,board,word,0)
                
if __name__ == "__main__":
    s = Solution()
    
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    result=s.exist(board,word)
    print(result)
    # print(True or False)
