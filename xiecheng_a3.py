number=10072

string_number=str(number)

# 以当前的数字为中心，向后面的数字扩展，看current_number%72是否为0（当current_number不为0的时候）
# 中心法

# 如何优化运行时间? 
index=0
length=len(string_number)
answer=0
answer_list=[]

while index<length:
    cur_number=string_number[index]
    if cur_number!="0":
        for i in range(index+1,length):
            cur_number+=string_number[i]
            if int(cur_number) in answer_list:
                answer+=1
            elif int(cur_number)%72==0:
                answer_list.append(int(cur_number))
                answer+=1
    else:
        answer+=1
    index+=1

print(answer)
