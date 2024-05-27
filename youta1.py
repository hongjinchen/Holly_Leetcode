M=9

# 是否M是2的倍数，不是则输出-1
if M%2!=0:
    print(-1)
else:
    # 遍历找到M小于2的a次方
    a=0
    while 2**a<M:
        a=a+1
    a=a-1
    
    rest=M-2**a
    
    # 为剩余數字遍历
    b=0
    
    while 2**b<rest:
        b=b+1
    
    if rest==2**b:
        print(b,a)
    else:
        print(-1)

    
        
    
    
