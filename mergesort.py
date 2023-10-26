def merge_sort(arr):
    # 基本情况：当数组长度为 1 或 0 时，数组已经是有序的
    if len(arr) <= 1:
        return arr
    
    # 分治步骤：将数组分成两半
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 递归地对两半进行排序
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # 合并两个有序数组
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    # 比较两个数组的元素并添加到结果数组中
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 如果左边数组还有剩余元素，将它们添加到结果数组中
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # 如果右边数组还有剩余元素，将它们添加到结果数组中
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

# 示例
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
