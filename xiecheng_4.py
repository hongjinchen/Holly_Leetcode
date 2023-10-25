length_a=3
length_b=2
b=['2', '3']

# 这是一个排列组合问题，根本的问题在于，如果length_a大于length_b，多的数字如果插入b可以有多少种可能性？
# 这道题我可以看做b=['2', '3']中可以插在'2'左，'2'右，'3'右
# 由于要求数组中都是正整数，所以插入的数值不能小于0
# 而在取数字的时候是有限制的，b[-1]之后的数值得是单调递减的，不然会加入进来，而b[0]之前的数值得是小于它的，并且只有一个（因为如果出现1,1/1,2这样的情况b[0]就不是第一个了）
# 中间的则是根据两个值的差值来确定能够插入的范围,首先必须小于前一个并且也小于后一个,并且相同的数字插入的数量不能大于1

need_n=length_a-length_b
# 需要插入几个数字

# 遍历b来查看有几种插入的方式
pre_one=-1
answer=0
    
# 动态规划

def dp(b,index,numbers):
    if numbers==0:
        return 1
    res=0
    for i in range(1,int(b[index])):
        res+= dp(b,index+1,numbers-1)+dp(b,index,numbers-1)
    return res
print(dp(b,0,length_a-length_b))