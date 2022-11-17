logs = ["d1/","../","../","../"]
level_number=0
for item in logs:
    #确认层级（到主文件夹的），根据item的含义对层级进行加减，
    # 比如是item不是"../"或者"./"样式，就判定它+1
    # 如果是../，-1
    # 如果是./，数字不变
    if item =="../":
        if level_number==0:
            level_number=level_number
        else:
            level_number=level_number-1
    elif item =="./":
        level_number=level_number
    else:
        level_number=level_number+1
print(level_number)
