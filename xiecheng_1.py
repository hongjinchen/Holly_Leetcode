s="abcde"
q=3
q_list=[['1', '2', '4'], ['2', '1', 'rca'], ['2', '0', 'a']]

for item in q_list:
    if item[0]=='1':
        start_index=int(item[1])
        end_index=int(item[2])
        s=s[:start_index-1]+s[end_index:]
        # 操作1
    else:
        index=int(item[1])
        s=s[:index]+item[2]+s[index:]
        # 操作2
print(s)
