merge_list=[1,4,6,7,3,4,9]

def mergeSort(list):
    length=len(list)
    first_list=list[:int(length/2)]
    second_list=list[int(length/2):]
    first_list