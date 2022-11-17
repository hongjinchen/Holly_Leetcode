s = "AB"
numRows = 1
index=0
level_index=0
level_list = []
result=""
if len(s)==1:
    return s
if numRows==1:
    return s
#针对整个字符串进行处理，假设numRows=3，那么while(s.length>0)时，
# 把第一个字符添加到level_list[0]里，把第二个字符添加到level_list[1]里
# 最后将level_list的三个字符串拼接成一个字符串
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

print(result)

#i%(2n-2) == 0 ----> row0

#i%(2n-2) == 1 & 2n-2-1 ----> row1

#i%(2n-2) == 2 & 2n-2-2 ----> row2

#...

#i%(2n-2) == n-1 ----> row(n-1)

#==>

#对 k = i%(2n-2)进行判断

#k<=n-1时候，s[i]就属于第k行
#k>n-1时候，s[i]就属于2n-2-k行