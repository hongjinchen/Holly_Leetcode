def bubble_sort(arr):
    n=len(arr)
    # 遍历整个数组，比较相邻的两个元素，如果它们是逆序的，则交换它们。
    for i in range(n):
        switch=False
        # 重复这个过程，每次遍历少看一个元素。
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                switch = True
        # 如果一次遍历中没有发生任何交换，则数组已经是有序的，可以提前结束算法。
        if not switch:
            break
    
    return arr

array=[1,3,4,2,7,9,5]
print(bubble_sort(array))
    
    
    