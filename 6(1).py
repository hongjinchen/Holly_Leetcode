class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index=0
        level_index=0
        level_list = []
        result=""
        if len(s)==1:
            return s
        if numRows==1:
            return s
#i%(2n-2) == 0 ----> row0

#i%(2n-2) == 1 & 2n-2-1 ----> row1

#i%(2n-2) == 2 & 2n-2-2 ----> row2

#...

#i%(2n-2) == n-1 ----> row(n-1)

#==>

#对 k = i%(2n-2)进行判断

#k<=n-1时候，s[i]就属于第k行
#k>n-1时候，s[i]就属于2n-2-k行
        for num in range(numRows):
            level_list.append("")
        while (len(s) > 0):
            if index%(2*numRows-2)<=numRows-1:
                level_index=index%(2*numRows-2)
            else:
                level_index=2*numRows-2-index%(2*numRows-2)
            if len(s)==0:
                break
            level_list[level_index] = level_list[level_index] + s[0]
            s = s[1:]
            index=index+1
        for item in level_list:
            result=result+item
        return(result)

#i%(2n-2) == 0 ----> row0

#i%(2n-2) == 1 & 2n-2-1 ----> row1

#i%(2n-2) == 2 & 2n-2-2 ----> row2

#...

#i%(2n-2) == n-1 ----> row(n-1)

#==>

#对 k = i%(2n-2)进行判断

#k<=n-1时候，s[i]就属于第k行
#k>n-1时候，s[i]就属于2n-2-k行
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solution=Solution()
    print(solution.convert(s,numRows))