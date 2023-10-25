plan_list=[['1', '5'], ['1', '6'], ['1', '7'], ['3', '8']]
k=3
n=4

if k==0:
    print(0)
    # 如果不能采用方案
else:
    # largest_one=-1
    # 根据期待值排序
    city_list={}
    for item in plan_list:
        if item[0] not in city_list:
            city_list[item[0]]=[item[1]]
        else:
            city_list[item[0]].append(item[1])
    
    
    answer_List=[0]
    for key in city_list:
        list=city_list[key]
        orgin_length=len(list)
        while len(list)>0:
            max_list=int(max(list))
            
            if max_list*2>min(answer_List) and len(list)==orgin_length:
                answer_List.append(max_list*2)
                list.remove(str(max_list))
            elif max_list>min(answer_List) and  len(list)!=orgin_length:
                answer_List.append(max_list)
                list.remove(str(max_list))
            else:
                break
    answer=0
    answer_List.sort()
    answer_List=answer_List[:k+1]
    for item in answer_List:
        answer+=item
    print(answer)


        # if int(item[1])>=largest_one:
        #     new_answer_List=[0]*k
        #     index_l=0
        #     while index_l<k-1:
        #         new_answer_List[index_l+1]=answer_List[index_l]
        #         index_l+=1
        #     new_answer_List[0]=item
        #     answer_List=new_answer_List

    # city_list=[]
    # answer=0
    # for city in answer_List:
    #     if city[0] not in city_list:
    #         answer+= int(city[1])*2
    #         city_list.append(city[0])
    #     else:
    #         answer+= int(city[1])
    # print(answer_List)
    # print(answer)

