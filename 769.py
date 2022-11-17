#给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。

#我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。

#返回数组能分成的最多块数量。
arr = [1,0,2,3,4]
copyarr=arr
index=1
answer=1
#初次切割
while len(copyarr)!=0:
    newArr=copyarr[index:] 
    newArrTwo=copyarr[:index] 
    newArrsort=sorted(newArr)
    newArrTwosort=sorted(newArrTwo)
    print(newArrTwo)
    if len(newArrsort)>0:
        if newArrTwosort[len(newArrTwosort)-1]>newArrsort[0]:
            index=index+1
        else:
            index=1
            answer=answer+1
            copyarr=newArr
    else:
        break
print(answer)  
