a_list=['3', '4', '7', '8', '10']
n=5

b_list=[]
for i in range(1,n):
    number=0
    while i*number<=int(a_list[i-1]):
        number+=1
    b=i*number-int(a_list[i-1])
    if b not in b_list:
        b_list.append(b)
    else:
        b=i*(number+1)-int(a_list[i-1])
        b_list.append(b)

print(b_list)