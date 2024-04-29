number_list=[['a', 'b', 'b'], ['a', 'a', 'c']]
n=2
m=3

answer=0
if n<2 or m<2:
    print(0)
else:
    # 寻找2*2矩阵区域特殊
    for index_m in range(0,m-1):
        # 从左到右
        for index_n in range(0,n-1):
        # 从上到下
        # 选中一个矩阵
            matrix=[number_list[index_n][index_m],number_list[index_n][index_m+1],number_list[index_n+1][index_m],number_list[index_n+1][index_m+1]]
            if len(set(matrix))==4:
                # 为不相同的，set会去重
                answer=answer+1
        print(answer)
    