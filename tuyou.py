string="aaaaaaa"

length=len(string)


if length==0:
    print(0)
elif  length==1:
    print(1)
    
else:
    if length>2:
        string+=string
    length=len(string)
    # 使用两个字符串相连来模仿环形
    # 环形--所以使用自己定的length来终止
    # 寻找最长的相同的子字符串
    max_length=0
    pre_char=""

    # 快慢指针
    slow=0
    fast=0
    while fast<length:
        if string[slow]==string[fast]:
            fast+=1
            # 两个相等
        else:
            # 不相等
            if (fast-slow)>max_length:
                max_length=fast-slow
            slow=fast
            fast+=1

    print(max(max_length,fast-slow))