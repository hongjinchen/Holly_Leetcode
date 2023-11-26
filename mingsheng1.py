n=4
k=3
string1="abcd"
string2="cdef"

if len(string1)!=len(string2):
    print("NO")
else:
    # 检验对应位置上的字符对转换次数
    dict_string={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    list_number=[]
    for index in range(n):
        list_number.append(abs(dict_string[string1[index]]-dict_string[string2[index]])%26)
    
    num=list_number[0]
    for item in list_number:
            if item!=num:
                print("NO")
                break
            if abs(item)>k:
                print("NO")
                break
    else:
        print("YES")                
         
    