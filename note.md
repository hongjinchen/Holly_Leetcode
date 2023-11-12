

# ACM模式

https://www.programmercarl.com/qita/acm.html



# 二分法

二分算法（Binary Search Algorithm），比较集合中间元素与目标元素，根据比较结果来消除一半的搜索空间。

1. **初始化指针**: 设定两个指针，`low` 和 `high`，分别指向集合的首尾。

2. **计算中点**: 在循环内，计算 `mid = (low + high) // 2`。

3. **比较**: 比较集合中间点 mid 的元素与目标元素。
   
   - 如果 `mid` 元素等于目标，搜索成功，返回 `mid` 的索引。
   - 如果 `mid` 元素小于目标，更新 `low = mid + 1`。
   - 如果 `mid` 元素大于目标，更新 `high = mid - 1`。
   
4. **重复**: 继续步骤2和3，直到 `low <= high` 不成立，或找到目标元素。

   

## 双指针法

1.

双指针法（Two-Pointer Technique）是一种常用于解决数组（Array）或链表（Linked List）问题的算法技巧。这种方法通过使用两个指针（或索引），通常从不同的方向遍历数组或链表，从而达到优化时间和/或空间复杂度的目的。



使用双指针的典型场景之一是你想要

**从两端向中间迭代数组。**

这时你可以使用双指针技巧：

**一个指针从头部开始，而另一个指针从尾部开始。**

这种技巧经常在排序数组中使用。



2.

有时，我们可以使用两个不同步的指针来解决问题，即快慢指针。与情景一不同的是，两个指针的运动方向是相同的，而非相反。

让我们从一个经典问题开始：

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

如果我们没有空间复杂度上的限制，那就更容易了。我们可以初始化一个新的数组来存储答案。如果元素不等于给定的目标值，则迭代原始数组并将元素添加到新的数组中。

实际上，它相当于使用了两个指针，一个用于原始数组的迭代，另一个总是指向新数组的最后一个位置。



**考虑空间限制**
如果我们不使用额外的数组，只是在原数组上进行操作呢？

此时，我们就可以采用快慢指针的思想：初始化一个快指针 fast 和一个慢指针 slow，fast 每次移动一步，而 slow 只当 fast 指向的值不等于 val 时才移动一步。



```python
def removeElement(self, nums: List[int], val: int) -> int:
    slow = 0
    n = len(nums)
    for fast in range(n):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```



### 相关题目

- #### 合并有序数组


1. 使用两个指针分别遍历两个有序数组。
2. 比较两个指针指向的元素，将较小的元素添加到结果数组中，并将对应的指针向前移动。
3. 如果一个数组遍历完了，将另一个数组剩余的元素添加到结果数组中。

合并两个有序数组是一个常见的算法问题，通常可以通过双指针法来解决。假设我们有两个有序数组 `A` 和 `B`，长度分别为 `m` 和 `n`。我们要将数组 `B` 合并到数组 `A` 中，并确保合并后的数组也是有序的。

以下是使用 Python 实现的代码：

```python
def merge_sorted_arrays(A, m, B, n):
    # 设置三个指针：p1 指向 A 的末尾，p2 指向 B 的末尾，p 指向合并后数组的末尾
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    # 当两个数组都还有元素时
    while p1 >= 0 and p2 >= 0:
        if A[p1] > B[p2]:
            A[p] = A[p1]
            p1 -= 1
        else:
            A[p] = B[p2]
            p2 -= 1
        p -= 1
    
    # 如果 A 中还有元素，那么它们已经是有序的并且在正确的位置
    # 所以我们只需要关心 B 中是否还有元素
    while p2 >= 0:
        A[p] = B[p2]
        p2 -= 1
        p -= 1

# 测试
A = [1, 3, 5, 0, 0, 0]
m = 3
B = [2, 4, 6]
n = 3

merge_sorted_arrays(A, m, B, n)
print(A)  # 输出应为 [1, 2, 3, 4, 5, 6]
```

在这里，我假设数组 `A` 有足够的空间来保存合并后的数组（也就是 `m + n` 的大小）。这是一个就地操作，也就是说我们没有使用额外的空间。

1. 我们从两个数组的末尾开始，使用三个指针：`p1`、`p2` 和 `p`。
2. `p1` 指向数组 `A` 中最后一个元素的位置，`p2` 指向数组 `B` 中最后一个元素的位置，`p` 指向数组 `A` 合并后最后一个元素应该放置的位置。
3. 我们比较 `p1` 和 `p2` 指向的元素，将较大的一个放到 `p` 指向的位置。
4. 然后，我们向左移动指针，重复步骤 3，直到 `p1` 或 `p2` 小于 0。
5. 最后，如果 `B` 中还有剩余的元素，我们需要将它们复制到 `A` 中相应的位置。



- #### 回文串判断 


其中一个指针从字符串开始处开始移动，另一个从字符串末尾开始移动。两个指针都只会经过一半的字符串，因此该算法的时间复杂度是 O(n/2)，即 O(n)。

```python
def is_palindrome(s: str) -> bool:
    # 移除字符串中的非字母和数字字符，并转为小写
    filtered_s = ''.join(filter(str.isalnum, s)).lower()
    
    # 使用双指针法进行回文检查
    left, right = 0, len(filtered_s) - 1
    while left < right:
        if filtered_s[left] != filtered_s[right]:
            return False
        left += 1
        right -= 1

    return True

# 测试
print(is_palindrome("A man a plan a canal Panama"))  # 输出应为 True
print(is_palindrome("race a car"))  # 输出应为 False
```



[33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

[34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)



- #### 时间复杂度

- 最好情况*O*(1)（目标元素就在集合的中间位置）
- 平均和最坏情况：O(logn)



# 动态规划

动态规划，英文：**Dynamic Programming**，简称DP，如果某一问题有很多重叠子问题，使用动态规划是最有效的。

所以动态规划中每一个状态一定是由上一个状态推导出来的，**这一点就区分于贪心**，贪心没有状态推导，而是从局部直接选最优的，



## 相关题目

[46. 全排列](https://leetcode.cn/problems/permutations/)

[47. 全排列 II](https://leetcode.cn/problems/permutations-ii/)

[53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)

> 给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
>
> 只用返回一个数字会比较适合dp解法，在这个题中是将球最大的数组和简化为在当前的index上，最大和为多少

[62. 不同路径](https://leetcode.cn/problems/unique-paths/)

[63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/)

[64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/)

### 青蛙跳台阶

问题描述：青蛙可以一次跳一个或两个台阶，问跳到第 `n` 个台阶有多少种跳法。

```python
def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 测试
print(climb_stairs(3))  # 输出应为 3
print(climb_stairs(4))  # 输出应为 5
```



# 分治法

分治法（Divide and Conquer）是一种常见的算法设计范式，其中一个典型的例子是**归并排序（Merge Sort）**。归并排序是一种高效、稳定的排序算法，它将一个大问题拆分成几个小问题，并递归解决这些小问题。具体地，归并排序将一个大数组分成两个（或更多）小数组，分别对这些小数组进行排序，最后再将它们合并成一个有序数组。



## 代码示例

```python
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
```

在这个例子中：

- `merge_sort` 函数负责将输入数组拆分成更小的数组，并递归地对它们进行排序。
- `merge` 函数负责将两个已排序的数组合并成一个新的有序数组。

这样，通过将大问题拆分成小问题，并将小问题的解决方案合并为大问题的解决方案，分治法实现了对数组的高效排序。



# 递归

## Memoization

在递归算法中使用`memo`字典来保存已经计算过的子问题的解的技术被称为“记忆化”（Memoization）。这是一种优化技术，用于通过存储昂贵的函数调用结果来避免重复计算，从而提高算法的运行速度。

记忆化是动态规划（Dynamic Programming, DP）中的一个常用手法。事实上，很多时候动态规划问题首先可以通过一个朴素的、没有优化的递归算法来解决。然后，通过添加记忆化，我们可以显著提高其效率。

简而言之，记忆化是一种特定类型的缓存策略，用于提高递归算法或者动态规划算法的效率。它通过保存已经解决的子问题的结果来避免重复工作。

Example:

```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        
        def DFS(l,r):
            if l>=r:
                return 1
            res = 0
            for i in range(l,r+1):
                res += DFS(l,i-1)*DFS(i+1,r)
            return res
        
        return DFS(1,n)
```

```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # 创建一个字典（或者数组）来存储已经计算过的值
        memo = {}

        def DFS(l, r):
            if l >= r:
                return 1

            # 检查是否已经计算过这个值
            if (l, r) in memo:
                return memo[(l, r)]

            res = 0
            for i in range(l, r+1):
                res += DFS(l, i-1)*DFS(i+1, r)
                # 将计算过的值存储在字典中
            memo[(l, r)] = res
            return res

        return DFS(1, n)
```

使用memo（记忆化）的核心思想是保存已经计算过的子问题的解，以便在将来需要时可以直接使用，**从而避免重复计算**。这在递归算法中尤其有效，因为递归算法往往会多次计算相同的子问题。

考虑numTrees(19)这个例子，它需要计算的子问题涉及的范围是[1, 19]。这样的子问题数量本身就是非常多的。如果没有记忆化，那么相同的子问题（同样的(l, r)值对）会被多次重新计算，导致大量的时间浪费。

例如，考虑子问题DFS(1, 18)和DFS(2, 19)。两者都需要计算DFS(2, 18)作为其子问题之一。在没有记忆化的情况下，DFS(2, 18)会被重新计算两次，而使用记忆化后，DFS(2, 18)只会被计算一次，其结果会被保存起来供以后使用。

这样的重复子问题在整个计算过程中会出现非常多次。通过记忆化，我们可以大大减少这些重复计算，从而显著提高算法效率。

记忆化通常能将时间复杂度从指数级（或更高）降低到多项式级。在这个具体的例子中，记忆化能够将算法的时间复杂度降低到O(n^2)（这里 n=19），这对于n=19来说是完全可接受的。

所以，使用memo字典节省了大量时间，使得即使对于较大的n值（如19），算法也能在合理的时间内运行完成。



## 经典问题

阶乘问题

二叉树深度

汉诺塔问题

斐波那契数列

快速排序、归并排序、分治算法

https://zhuanlan.zhihu.com/p/338302261



## 相关题目



# 排序问题

## 常用的排序算法

### **冒泡排序（Bubble Sort）**

- #### 基本思路


1. 遍历整个数组，**比较相邻的两个元素，如果它们是逆序的，则交换它们。**

2. 重复这个过程，**每次遍历少看一个元素。**

3. **如果一次遍历中没有发生任何交换，则数组已经是有序的，可以提前结束算法。**

   

- #### 时间复杂度和空间复杂度


- 时间复杂度：O(n^2)

- 空间复杂度：O(1)

- 稳定性：稳定

  

- #### 示例代码（Python）


```java
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
```



- #### 初始状态:

```
[5, 3, 8, 4, 2]
```

**第一轮冒泡（最大的元素会被放到最后）:**

- 比较5和3，5大于3，交换位置: `[3, 5, 8, 4, 2]`
- 比较5和8，5小于8，不交换: `[3, 5, 8, 4, 2]`
- 比较8和4，8大于4，交换位置: `[3, 5, 4, 8, 2]`
- 比较8和2，8大于2，交换位置: `[3, 5, 4, 2, 8]`

经过第一轮后，最大的数8已经在正确的位置。



**第二轮冒泡（第二大的元素会被放到倒数第二位）:**

- 比较3和5，3小于5，不交换: `[3, 5, 4, 2, 8]`
- 比较5和4，5大于4，交换位置: `[3, 4, 5, 2, 8]`
- 比较5和2，5大于2，交换位置: `[3, 4, 2, 5, 8]`

现在，5和8已经在正确的位置。



**第三轮冒泡（第三大的元素会被放到倒数第三位）:**

- 比较3和4，3小于4，不交换: `[3, 4, 2, 5, 8]`
- 比较4和2，4大于2，交换位置: `[3, 2, 4, 5, 8]`

现在，2, 4, 5, 8都在正确的位置。



**第四轮冒泡（排序完成）:**

- 比较3和2，3大于2，交换位置: `[2, 3, 4, 5, 8]`

至此，整个数组已经完全排序。



**最终排序后的数组:**

```
[2, 3, 4, 5, 8]
```

这个简单的例子说明了冒泡排序每一步如何通过相邻元素的比较和交换来逐步将**最大元素“冒泡”到数组的末端**。排序过程中，每一轮遍历都会确定一个元素的最终位置，直到全部元素都被排序。



- #### 例题


[75. 颜色分类](https://leetcode.cn/problems/sort-colors/)



### **归并排序（Merge Sort）**

- #### 基本思路


1. 分：将原始数组分成**两个或更多的空间。**

2. 解决：**递归地将子数组排序。**

3. 合并（Merge）：**将排序后的子数组合并，形成一个新的排序数组。**

   

- #### 时间复杂度和空间复杂度


- 时间复杂度：O(n log n)

- 空间复杂度：O(n)

- 稳定性：稳定

  

- #### 示例代码（Python）


```python
def merge_sort(arr):
    # 如果数组长度小于或等于 1，那么它已经是有序的
    if len(arr) <= 1:
        return arr
    
    # 计算中点并分割数组为两个子数组
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 递归地对两个子数组进行排序
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # 将两个已排序的子数组进行归并
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0
    
    # 比较 left 和 right 数组中的元素，并添加到结果数组中
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 如果 left 数组还有剩余元素，将其添加到结果数组中
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # 如果 right 数组还有剩余元素，将其添加到结果数组中
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

# 测试归并排序函数
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print("Sorted Array:", sorted_arr)
```

让我们以一个具体的数组为例，展示归并排序的过程。考虑以下数组：

```
[38, 27, 43, 3, 9, 82, 10]
```

我们将逐步进行归并排序：

- #### 初始状态:

```
[38, 27, 43, 3, 9, 82, 10]
```

- #### 分割数组:

首先将数组**分割成最小单元，直到每个子数组只含有一个元素。**

```
[38, 27, 43, 3]    [9, 82, 10]
[38, 27] [43, 3]   [9, 82] [10]
[38] [27] [43] [3] [9] [82] [10]
```

- #### 合并数组:

接下来，我们开始合并子数组，同时排序它们。

```
[38] [27]    [43] [3]    [9] [82]    [10]
[27, 38]     [3, 43]     [9, 82]     [10]
```

**合并子数组时，我们逐个比较各自的元素，并按顺序放入新数组：**

```
[3, 27, 38, 43]    [9, 10, 82]
```

最后，合并最终的子数组，得到排序后的数组：

```
[3, 9, 10, 27, 38, 43, 82]
```

- #### 完整过程展示：

1. 拆分数组，直到子数组只含有单一元素。
2. 按顺序重新组合子数组，比较各个元素，将它们排序。
3. 继续合并上一步的结果，直到所有子数组都合并成一个完整的数组。

整个排序过程的伪代码可以表示如下：

```
拆分过程：
[38, 27, 43, 3, 9, 82, 10]
[38, 27, 43, 3]    [9, 82, 10]
[38, 27] [43, 3]   [9, 82] [10]
[38] [27] [43] [3] [9] [82] [10]

合并过程：
[27, 38] [3, 43]   [9, 82] [10]
[3, 27, 38, 43]    [9, 10, 82]
[3, 9, 10, 27, 38, 43, 82]
```





### **快速排序（Quick Sort）**

**快速排序（Quick Sort）**是一种被广泛应用的排序算法，由英国计算机科学家 Tony Hoare 在1960年提出。它是一种分治法（Divide and Conquer）的应用，能够在平均情况下实现 O(n log n) 的时间复杂度。下面是快速排序的基本思路和详细解释。

**基本思路**

1. **选取基准元素（Pivot）**: 在数组中选择一个元素作为基准。
   2. **分区（Partitioning）**: 重新排列数组，使得比基准元素小的元素在其左侧，比基准元素大的元素在其右侧。在这一过程中，基准元素到达其最终位置。
   3. **递归排序子数组**: 对基准元素左右两侧的子数组进行同样的操作。
   4. **结束条件**: **当子数组的大小为 0 或 1 时，该子数组已经是有序的，不需要进一步处理。**
   

**算法步骤**

假设我们有一个数组 `arr = [3, 6, 8, 10, 1, 2, 1]`，并且我们选择最后一个元素作为基准元素。

1. **选取基准元素**:
   
   - 我们选择 `1` 作为基准元素。
   2. **分区**:
      - 定义两个指针 `i` 和 `j`。其中，`i` 从数组的第一个元素开始，`j` 从数组的倒数第二个元素开始。
      - 遍历数组，使得所有小于 `1` 的元素都移到它的左侧，所有大于 `1` 的元素都移到它的右侧。
      - 例如，我们可能得到一个这样的数组：`[1, 1, 8, 10, 3, 6, 2]`。
      - 现在，基准元素 `1` 已经到达了它应该在的位置。
   3. **递归排序子数组**:
      - 对于基准元素左侧的子数组 `[1]` 和右侧的子数组 `[8, 10, 3, 6, 2]`，我们递归地进行快速排序。
   4. **结束条件**:
      - 当递归到数组大小为 0 或 1 时，递归结束。
   

**代码示例（Python）**

```python
   def quick_sort(arr, low, high):
       if low < high:
           # 找到基准元素后的正确位置
           pivot_index = partition(arr, low, high)
           
           # 递归地对基准元素左边和右边的子数组进行快速排序
           quick_sort(arr, low, pivot_index - 1)
           quick_sort(arr, pivot_index + 1, high)
   
   def partition(arr, low, high):
       # 选择最右侧的元素作为基准
       pivot = arr[high]
       i = low - 1
       
       # 将小于基准的元素移动到基准的左侧
       for j in range(low, high):
           if arr[j] < pivot:
               i += 1
               arr[i], arr[j] = arr[j], arr[i]
               
       # 将基准元素移动到正确的位置
       arr[i + 1], arr[high] = arr[high], arr[i + 1]
       return i + 1
   
   # 测试快速排序函数
   if __name__ == "__main__":
       arr = [10, 7, 8, 9, 1, 5]
       n = len(arr)
       quick_sort(arr, 0, n - 1)
       print("Sorted array:", arr)
   
```

**时间复杂度和空间复杂度**

- **时间复杂度**
     - 最好情况：O(n log n)
     - 平均情况：O(n log n)
     - 最坏情况：O(n^2)
   - **空间复杂度**: O(log n) 到 O(n)
   



**快速排序过程：**

假设我们有以下数组需要排序：

```
[10, 80, 30, 90, 40, 50, 70]
```

- #### 初始状态:

```
[10, 80, 30, 90, 40, 50, 70]
```

选择数组的最后一个元素作为基准值（pivot），这里是70。

- #### 第一次分区后：

将比70小的数移到左边，比70大的数移到右边，分区完成后，基准值的位置在这两个部分的中间。

```
[10, 30, 40, 50, 70, 90, 80]
```

基准值70现在在正确的位置上了。

- #### 对左侧子数组 `[10, 30, 40, 50]` 进行快速排序：

选择50作为基准值，经过分区操作后，我们得到：

```
[10, 30, 40, 50]
```

在这个子数组中，50已经被放到了正确的位置。

- #### 对右侧子数组 `[90, 80]` 进行快速排序：

选择80作为基准值，经过分区操作后，我们得到：

```
[80, 90]
```

此时，80和90都已经在正确的位置上了。

- #### 最终排序后的数组:

```
[10, 30, 40, 50, 70, 80, 90]
```

整个数组现在是有序的。



### **选择排序（Selection Sort）**

**基本思路**

选择排序（Selection Sort）是一种简单直观的排序算法。它的工作原理是每次从**未排序的元素中找出最小（或最大）元素**，将其**存放到序列的起始（或末尾）位置**。这样，每次迭代后，**最小（或最大）元素就被放到了它最终排序后应处于的位置**。该过程会持续进行，直到所有元素都被正确排序。

**时间复杂度和空间复杂度**

- 时间复杂度：O(n^2)
- 空间复杂度：O(1)
- 稳定性：不稳定

**示例代码（Python）**

```python
def selection_sort(arr):
    n = len(arr)
    
    # 遍历整个数组
    for i in range(n):
        # 找到从当前位置到数组末尾的最小元素的索引
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # 交换找到的最小元素和当前位置的元素
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 测试选择排序函数
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print("Sorted array:", arr)
```



假设我们有以下一组数字需要进行选择排序：

```
[64, 25, 12, 22, 11]
```

下面是排序的详细步骤：

- #### 初始状态:

```
[64, 25, 12, 22, 11]
```

- #### 第一轮选择排序：

找出最小的元素11，它位于最后的位置，与第一个元素64交换位置。

```
[11, 25, 12, 22, 64]
```

- #### 第二轮选择排序：

在剩下的元素中（25, 12, 22, 64），12是最小的，与25（数组的第二个元素）交换位置。

```
[11, 12, 25, 22, 64]
```

- #### 第三轮选择排序：

在剩下的元素中（25, 22, 64），22是最小的，它已经在正确的位置，所以不做任何操作。

```
[11, 12, 22, 25, 64]
```

- #### 第四轮选择排序：

在最后两个元素中（25, 64），25已经在正确的位置，不做任何操作。最大的元素64自然就在最后的位置了。

```
[11, 12, 22, 25, 64]
```

经过上述四轮排序后，数组变成了有序状态。每一轮排序确定了一个元素的最终位置。

- #### 最终排序后的数组:

```
[11, 12, 22, 25, 64]
```

以上就是选择排序的整个过程。在这个例子中，数组中的每个元素都被检查了以确定它们的最终位置。尽管选择排序的平均时间复杂度为O(n^2)，它在处理小规模或基本有序的数据时还是非常有用和高效的。



### **插入排序（Insertion Sort）**

- #### 基本思路


1. 从第一个元素开始，该元素可以认为已经被排序。

2. **取出下一个元素，在已经排序的元素序列中从后向前扫描。**

3. 如果该元素（已排序）大于新元素，**将该元素移到下一位置。**

4. 重复步骤3，直到找到已排序的元素小于或等于新元素的位置。

   

- #### 时间复杂度和空间复杂度


- 时间复杂度：O(n^2)

- 空间复杂度：O(1)

- 稳定性：稳定

  

- #### 示例代码（Python）


```java
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```



排序过程：

假设我们有以下数组需要排序：

```
[29, 10, 14, 37, 13]
```

- #### 初始状态:

```
[29, 10, 14, 37, 13]
```
我们从第二个元素开始，将29视为已排序。

- #### 第一轮插入排序：

我们看第二个元素10，它比29小，所以我们将10移动到第一个位置。

```
[10, 29, 14, 37, 13]
```

- #### 第二轮插入排序：

下一个元素是14，它比29小，但比10大。我们将14插入到10和29之间。

```
[10, 14, 29, 37, 13]
```

- #### 第三轮插入排序：

下一个元素是37，它比29大，所以它已经在正确的位置，不需要移动。

```
[10, 14, 29, 37, 13]
```

- #### 第四轮插入排序：

最后一个元素是13，它比37、29小，但比14大。我们将13插入到14和29之间。

```
[10, 13, 14, 29, 37]
```

- #### 最终排序后的数组:

```
[10, 13, 14, 29, 37]
```

排序完成后，数组已经是有序的。插入排序对于小规模数据或基本有序的数据效率很高，它是一种稳定的排序算法，时间复杂度为O(n^2)。尽管对于大规模的无序数据效率不是很高，但是它的实现简单，对于小数据集来说是一个不错的选择。



## 稳定性

在讨论排序算法时，“稳定性”是一个重要的特性。稳定排序算法与不稳定排序算法的区别主要在于它们**是否保持相等元素的相对顺序。**

- #### **稳定排序算法**

如果一个排序算法能够**保证两个相等的元素在排序前后的相对顺序不变，那么这个排序算法就是稳定的**。在稳定排序算法中，如果元素A在元素B之前，并且A = B，那么排序后A仍然在B之前。

稳定排序的例子：
- **插入排序**：在将元素插入已排序的部分时，插入排序总是将当前元素放在相等元素的后面，从而保持了元素间的相对顺序。
- **冒泡排序**：每次通过交换相邻的元素来“冒泡”最大（或最小）的元素到序列的一端，这个过程保持了相等元素的相对位置。
- **归并排序**：在合并两个已排序数组的时候，如果出现相等的元素，总是先拷贝前面数组（左边数组）的元素，这样保持了元素的相对顺序。
- **计数排序**：由于它是通过计数而非比较来确定元素的最终位置，计数排序也能保持相等元素的原始顺序。



- #### 不稳定排序算法

不稳定排序算法**不能保证两个相等的元素在排序前后的相对顺序不变**。这意味着如果有两个相等的元素A和B，且在排序前A在B前面，排序后B可能会在A前面。

不稳定排序的例子：
- **选择排序**：在每次找到最小（或最大）元素时，选择排序会直接将它与序列中当前位置的元素交换，不考虑这个元素之前是否有相等的元素。
- **希尔排序**：作为插入排序的一种变体，希尔排序通过比较相隔一定间隔的元素来进行排序，这可能会打乱相等元素的初始顺序。
- **堆排序**：堆排序通过构建堆结构来排序，由于堆的性质，当调整堆时可能会改变相等元素的相对顺序。
- **快速排序**：在分区过程中，相等的元素可能会根据它们的位置不同而被移动到枢轴的任一侧，从而导致它们的相对顺序发生变化。

在某些应用场景下，稳定性可能是一个重要的要求。例如，**在处理具有多个字段的数据时，可能需要保持前一个排序操作的结果，这时稳定排序就显得尤为重要。如果算法不稳定，可能需要采用额外的逻辑来保持所需的顺序。**



## 例题

- #### **合并所有的重叠区间，合并后的区间按照升序排列** 

合并所有重叠区间并按照升序排列是一个经典的算法问题，通常用于间隔调度、时间表生成等场景。这个问题的解决方法一般分为以下几个步骤：

**步骤：**

1. **排序**：首先对给定的区间按照起始点进行排序。

2. **初始化**：将第一个区间添加到结果列表中。

3. 合并

   ：遍历其余的区间，与结果列表中最后一个区间进行比较，看是否有重叠。

   - 如果有重叠，合并它们。
   - 如果没有重叠，直接将当前区间添加到结果列表中。

4. **输出**：返回合并后的结果列表。

**Python 代码示例：**

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # 按区间的起始点进行排序
    intervals.sort(key=lambda x: x[0])
    
    # 初始化结果列表，并将第一个区间添加进去
    result = [intervals[0]]
    
    # 遍历剩下的区间
    for current in intervals[1:]:
        # 获取结果列表中最后一个区间
        last = result[-1]
        
        # 检查当前区间和最后一个区间是否有重叠
        if current[0] <= last[1]:
            # 合并两个重叠的区间
            result[-1] = [last[0], max(last[1], current[1])]
        else:
            # 如果没有重叠，直接添加到结果列表中
            result.append(current)
    
    return result

# 测试代码
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Merged intervals:", merge_intervals(intervals))
```

运行这段代码后，输出的合并后的区间应该是 `[[1, 6], [8, 10], [15, 18]]`。

这个算法的时间复杂度是 O*(*n*log*n*)，主要消耗在排序步骤上。空间复杂度则为 O*(*n*)，用于存储结果列表。



# 回溯算法和DFS

回溯算法是一种用于找到所有（或某些）可能解决方案的算法，特别是在涉及约束满足问题（Constraint Satisfaction Problems，CSP）的情况下。回溯算法的核心思想是从问题的可能解决方案的空间树中，按照深度优先搜索（DFS）的策略，从根节点出发遍历解空间树。

**深度优先搜索算法（Depth First Search，简称DFS）**：一种用于遍历或搜索树或图的算法。 沿着树的深度遍历树的节点，尽可能深的搜索树的分支。当节点v的所在边都己被探寻过或者在搜寻时结点不满足条件，搜索将**回溯**到发现节点v的那条边的起始节点。整个进程反复进行直到所有节点都被访问为止。属于盲目搜索,最糟糕的情况算法时间复杂度为O(!n)。

1. 为了求得问题的解，先选择某一种可能情况向前探索；
2. 在探索过程中，一旦发现原来的选择是错误的，就退回一步重新选择，继续向前探索；
3. 如此反复进行，直至得到解或证明无解。

### 算法步骤

1. **初始状态**：一般来说，所有的节点都是未访问状态。
2. **选择起点**：选择一个起点作为当前节点。
3. **标记当前节点**：将当前节点标记为已访问。
4. **检查邻接点**：
   
   - 查找当前节点的所有未访问的邻接点。
   - 如果当前节点存在未访问的邻接点，则选择其中一个，作为当前节点，并回到步骤3。
   - 如果当前节点没有未访问的邻接点，则回溯到上一个节点，并将其设置为当前节点。
5. **终止条件**：
   - 所有可访问的节点都已访问。
   
   - 找到目标节点（如果有）。
   
   - 手动终止。
   
      **模板**
   
     ```java
     void backtracking(参数) {
         if (终止条件) {
             存放结果;
             return;
         }
     
         for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
             处理节点;
             backtracking(路径，选择列表); // 递归
             回溯，撤销处理结果
         }
     }
     ```
   
     

### 应用场景

- 图遍历
- 路径搜索
- 拓扑排序
- 迷宫（或格网）问题
- 组合问题（如 N-皇后问题）

## 相关题目

[95. 不同的二叉搜索树 II](https://leetcode.cn/problems/unique-binary-search-trees-ii/)



# 数据结构

## 基础介绍

「线性数据结构」与「非线性数据结构」

<img src="https://pic.leetcode-cn.com/1599638810-SZDwfK-Picture1.png" alt="Picture1.png" style="zoom: 50%;" />



## 数组

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231020215226122.png" alt="image-20231020215226122" style="zoom:50%;" />

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231020215700924.png" alt="image-20231020215700924" style="zoom: 33%;" />

数组是**将相同类型的元素存储于连续内存空间的数据结构，其长度不可变。**

如下图所示，**构建此数组需要在初始化时给定长度，**并对数组每个索引元素赋值，代码如下：

```java
// 初始化一个长度为 5 的数组 array
int[] array = new int[5];
// 元素赋值
array[0] = 2;
array[1] = 3;
array[2] = 1;
array[3] = 0;
array[4] = 2;
```

或者可以使用直接赋值的初始化方式，代码如下：

```
int[] array = {2, 3, 1, 0, 2};
```



**ArrayList「可变数组」**是经常使用的数据结构，其基于组和扩容机制实现，相比普通数组更加灵活。常用操作有：**访问元素、添加元素、删除元素。**

Java

```java
// 初始化可变数组
List<Integer> array = new ArrayList<>();

// 向尾部添加元素
array.add(2);
array.add(3);
array.add(1);
array.add(0);
array.add(2);
```

Python

```python
# 初始化可变数组
array = []

# 向尾部添加元素
array.append(2)
array.append(3)
array.append(1)
array.append(0)
array.append(2)
```



### 数组越界

数组越界发生在当代码尝试访问数组的一个非法索引时，即这个索引超出了数组的当前分配的范围。在大多数编程语言中，数组的索引从0开始，并且一个数组拥有固定的大小。如果你试图访问一个超出这个范围的索引，将会发生越界错误。


数组越界可能发生在许多编程语言中，特别是在那些不自动进行边界检查的低级语言中。这里有几个例子：

1. **C/C++：** 这些语言不会自动检查数组边界。如果你尝试访问一个超出数组声明范围的索引，就会发生数组越界。由于没有内置的安全检查，这可能导致未定义行为，包括数据损坏和安全漏洞。
2. **Go：** 虽然Go是一种相对更安全的语言，但在默认情况下，它不会进行数组边界检查。当然，如果越界，它会在运行时抛出panic。
3. **Rust：** Rust在编译时和（或）运行时进行边界检查。如果使用的是索引访问方式（如`arr[i]`），并且索引越界，它将在运行时导致panic。Rust也提供了`.get()`方法，该方法在索引越界时返回`None`，而不是panic。
4. **Fortran：** 默认情况下，Fortran不会进行数组边界检查，但大多数现代Fortran编译器提供了编译时选项来启用它。

另一方面，许多高级语言提供了内置的数组边界检查：

1. **Java：** Java会在运行时自动检查数组边界，并在越界访问数组时抛出`ArrayIndexOutOfBoundsException`。

2. **Python：** Python在试图越界访问列表（相当于数组）时会抛出`IndexError`。

3. **C#：** C#也会在数组越界时抛出`IndexOutOfRangeException`。

4. **JavaScript：** 在JavaScript中，如果你尝试访问超出数组长度的索引，不会抛出错误，而是返回`undefined`。但是，如果尝试写入越界的索引，则会导致原始数组的自动扩展。

   

## 链表

链表以节点为单位，每个元素都是一个**独立对象**，在**内存空间的存储是非连续的**。链表的节点对象具有两个成员变量：**「值 val」，「后继节点引用 next」** 。

Java

```java
class ListNode {
    int val;       // 节点值
    ListNode next; // 后继节点引用
    ListNode(int x) { val = x; }
}
```

Python

```python
class ListNode:
    def __init__(self, x):
        self.val = x     # 节点值
        self.next = None # 后继节点引用
```

如下图所示，建立此链表需要实例化每个节点，并构建各节点的引用指向。

JAVA

```java
// 实例化节点
ListNode n1 = new ListNode(4); // 节点 head
ListNode n2 = new ListNode(5);
ListNode n3 = new ListNode(1);

// 构建引用指向
n1.next = n2;
n2.next = n3;
```



**相关题目**

[82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/)

[86. 分隔链表](https://leetcode.cn/problems/partition-list/)



**如何判断链表里有环**---**快慢指针法**

该算法使用两个指针，**一个快指针和一个慢指针**。快指针每次移动两个节点，而慢指针每次移动一个节点。如果链表中存在环，快慢指针最终会在环内的某个节点相遇。



**快慢指针法的终止条件：**

该算法有两个主要的终止条件：

1. **相遇条件**：如果快指针和慢指针在链表中的某个点相遇，这意味着链表存在环。
2. **空指针条件**：如果快指针或其下一个节点成为**空指针（`None`）**，这意味着链表没有环。



**Python 代码示例：**

下面是使用 Python 定义一个简单的链表节点和使用快慢指针法检测链表中是否存在环的代码：

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    # 初始化慢指针和快指针
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        # 慢指针移动一步
        slow = slow.next
        # 快指针移动两步
        fast = fast.next.next
        
        # 检查快慢指针是否相遇
        if slow == fast:
            return True  # 存在环
    
    return False  # 不存在环

# 创建一个没有环的链表
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# 测试函数
print("Has cycle:", has_cycle(head))  # 输出应为 False

# 创建一个有环的链表
head.next.next.next = head

# 测试函数
print("Has cycle:", has_cycle(head))  # 输出应为 True
```

在这个示例中，`ListNode` 类用于创建链表节点，`has_cycle` 函数则用于检测链表是否包含环。我们首先创建一个没有环的链表进行测试，然后修改链表以形成一个环，并再次进行测试。

这种使用快慢指针的方法时间复杂度为 O*(*n*)，其中 n 是链表中的节点数。空间复杂度为 O*(1)，因为我们只使用了两个指针。



## 栈（Stack）

1. **定义**：栈是一种**后进先出（LIFO，Last-In-First-Out）**的数据结构。

2. **操作**：主要有两种基本操作——**压栈（push）和弹栈（pop）**。

3. **应用**：函数调用、表达式求值、深度优先搜索等。

4. **存储**：通常使**用数组或链表**来实现。

5. **性能**：**压栈和弹栈操作通常是 O(1) 的时间复杂度。**

   

**示例代码（Python）**

```python
class Stack:
    def __init__(self):
        self.items = [] # Python 可将列表作为栈使用
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
```

**JAVA**

```java
Stack<Integer> stack = new Stack<>();

stack.push(1); // 元素 1 入栈
stack.push(2); // 元素 2 入栈
stack.pop();   // 出栈 -> 元素 2
stack.pop();   // 出栈 -> 元素 1

LinkedList<Integer> stack = new LinkedList<>();

stack.addLast(1);   // 元素 1 入栈
stack.addLast(2);   // 元素 2 入栈
stack.removeLast(); // 出栈 -> 元素 2
stack.removeLast(); // 出栈 -> 元素 1
```



## 队列

队列是一种具有 **「先入先出」** 特点的抽象数据结构，**可使用链表实现。**

Java

```java
Queue<Integer> queue = new LinkedList<>();
```

Python

```python
# Python 通常使用双端队列 collections.deque
from collections import deque

queue = deque()
```

如下图所示，通过常用操作「入队 push()」,「出队 pop()」，展示了队列的先入先出特性。

Java

```java
queue.offer(1); // 元素 1 入队
queue.offer(2); // 元素 2 入队
queue.poll();   // 出队 -> 元素 1
queue.poll();   // 出队 -> 元素 2
```

Python

```python
queue.append(1) # 元素 1 入队
queue.append(2) # 元素 2 入队
queue.popleft() # 出队 -> 元素 1
queue.popleft() # 出队 -> 元素 2
```



## 堆（Heap）

#### **定义**

**堆是一种特殊的完全二叉树，满足堆的性质（最大堆或最小堆）。**

> **完全二叉树；**
>
> **定义**
>
> 一个二叉树在除了最后一层以外的其余每一层都是完全填充的，并且所有节点都保持向左对齐，这样的二叉树称为完全二叉树。
>
> **特性**
>
> 1. **结构平衡**：在完全二叉树中，上面的层总是会在添加新节点之前填满。新节点总是从左到右添加。
>
> 2. **高度有限制**：对于有 *n* 个节点的完全二叉树，树的高度为 ⌊log2*n*⌋。
>
> 3. **叶子节点**：叶子节点只能出现在最后两层。在最后一层中，叶子节点集中在左侧。
>
>    
>
> **应用场景**
>
> 1. **堆（Heap）**：堆是一种特殊的完全二叉树，常用于实现优先队列。
>
> 2. **二叉树数组表示**：由于完全二叉树的特性，它特别适合用数组来表示。这样做可以节省存储空间，并且方便进行索引操作。
>
>    
>
> **代码示例**
>
> 用Python表示一个完全二叉树：
>
> ```
> class TreeNode:
>     def __init__(self, value=0, left=None, right=None):
>         self.value = value
>         self.left = left
>         self.right = right
> 
> # 创建一个完全二叉树
> #         1
> #       /   \
> #      2     3
> #     / \   / 
> #    4   5 6  
> root = TreeNode(1)
> root.left = TreeNode(2)
> root.right = TreeNode(3)
> root.left.left = TreeNode(4)
> root.left.right = TreeNode(5)
> root.right.left = TreeNode(6)
> ```

1. **操作**：插入元素、删除最大/最小元素等。

   #### 创建堆

   创建 堆 指的是初始化一个堆实例。所有堆方法的前提必须是在堆实例上进行操作。换句话说，我们必须要首先创建一个 堆 实例，然后才能使用 堆 的常用方法。在创建 堆 的过程中，我们也可以同时进行 堆化 操作。堆化 就是将一组数据变成 堆 的过程。

   时间复杂度： 
   O(N)。

   空间复杂度： 
   O(N)。

   ```python
   import heapq
   # 创建一个空的最小堆
   minHeap = []
   heapq.heapify(minHeap)
   
   # 创建一个空的最大堆
   # 由于Python中并没有内置的函数可以直接创建最大堆，所以一般我们不会直接创建一个空的最大堆。
   
   # 创建带初始值的「堆」， 或者称为「堆化」操作，此时的「堆」为「最小堆」
   heapWithValues = [3,1,2]
   heapq.heapify(heapWithValues)
   
   # 创建最大堆技巧
   # Python中并没有内置的函数可以直接创建最大堆。
   # 但我们可以将[每个元素*-1]，再将新元素集进行「堆化」操作。此时，堆顶元素是新的元素集的最小值，也可以转换成原始元素集的最大值。
   # 示例
   maxHeap = [1,2,3]
   maxHeap = [-x for x in maxHeap]
   heapq.heapify(maxHeap)
   # 此时的maxHeap的堆顶元素是-3
   # 将-3转换为原来的元素3，既可获得原来的maxHeap中最大的值是3
   ```

   **最小堆转换城最大堆的逻辑**

   **方法 1: 取反（Negation）**

   一种常见的技巧是在插入堆之前取每个元素的负值。因为 `heapq` 是最小堆，所以它会把负数排在最前面。因此，实际上负的负数（即原数）就成了最大数。

   **方法 4: 转换已有的最小堆为最大堆**

   如果你已经有一个最小堆，并且希望将其转换为最大堆，你可以这样做：

   1. 遍历整个最小堆，取每个元素的负值。

   2. 使用 `heapify` 函数重新堆化。

      

   #### 堆的插入步骤

   1. **添加元素**：将新元素添加到完全二叉树的最后一个位置，即数组的最后。这样做会保持完全二叉树的性质。
   2. **上浮（Heapify Up）**：比较新添加的元素与其父节点的值。
      - 如果新元素大于其父节点，那么交换它们。
      - 继续这个过程，直到新元素到达根节点或者其值小于（或等于）其父节点。

   这个过程也称为“堆化”（Heapify），它确保了堆的第二个性质：节点间的大小关系。

   插入操作的时间复杂度是O*(log*n)，这里 n是堆中元素的数量。

   ```python
   def heapify_up(heap):
       index = len(heap) - 1  # 新元素的索引位置
       while index > 0:
           parent_index = (index - 1) // 2  # 找到父节点的索引位置
           # 如果新元素大于父节点，则交换它们
           if heap[index] > heap[parent_index]:
               heap[index], heap[parent_index] = heap[parent_index], heap[index]
               index = parent_index  # 更新当前节点的索引为父节点的索引，继续上浮
           else:
               break  # 如果新元素小于或等于父节点，则停止上浮
   
   def insert(heap, value):
       heap.append(value)  # 在数组最后添加新元素
       heapify_up(heap)  # 上浮以保持堆的性质
   
   # 创建一个空的最大堆
   max_heap = []
   
   # 插入元素
   insert(max_heap, 3)
   insert(max_heap, 4)
   insert(max_heap, 9)
   insert(max_heap, 5)
   insert(max_heap, 2)
   
   print("Max Heap:", max_heap)  # 输出应该是一个最大堆
   ```

   

   #### 删除最大/最小元素

   删除操作是指在 **堆** 中删除堆顶元素。元素删除之后，**堆** 依旧需要维持它的特性。

   1. **替换根节点**：用堆的最后一个元素替换根节点。这样做可以轻易地维持堆的完全二叉树性质。

   2. **下沉（Heapify Down）**：从新的根节点开始，与其子节点进行比较：

      - 选取两个子节点中较大（对于最大堆）或较小（对于最小堆）的一个。
      - 如果该子节点大于（或小于）当前节点，则交换它们。
      - 继续这个过程，直到当前节点大于（或小于）其任何子节点，或者它成为叶子节点。

   3. **返回被删除的元素**：可选操作，通常是将最初的根节点（即被删除的最大或最小元素）返回给用户。

      

   #### 获取堆顶元素

   最大堆 的堆顶元素是 堆 中的最大值，最小堆 的堆顶元素是 堆 中的最小值。因此，堆顶元素是 堆 中最重要的元素。

   时间复杂度： 
   O(1)。

   空间复杂度：
   O(1)。

   ```
   # 最小堆获取堆顶元素，即最小值
   minHeap[0]
   # 最大堆获取堆顶元素，即最大值
   # 元素乘以 -1 的原因是：我们之前插入元素时，将元素乘以 -1，所以在获取元素时，我们需要乘以 -1还原元素。
   maxHeap[0]*-1
   ```

   

   #### 操作的复杂度

   <img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231024135350880.png" alt="image-20231024135350880" style="zoom:67%;" />

   

1. **应用**：优先队列、堆排序、图算法（如 Dijkstra 算法）等。

2. **存储**：在堆的数据结构中，我们常用堆的插入、删除、获取堆顶元素的操作。

   我们可以用**数组**实现堆。我们将堆中的元素以二叉树的形式存入在数组中。以下代码将使用数组实现整数类型的「最大堆」和「最小堆」，仅供大家参考（在实际解题或者工作中，一般很少需要自己去实现堆）：

   ```python
   # 「最小堆」的实现
   import sys
   
   class MinHeap:
       def __init__(self, heapSize):
           # heapSize用于数组的大小，因为数组在创建的时候至少需要指明数组的元素个数
           self.heapSize = heapSize
           # 使用数组创建完全二叉树的结构，然后使用二叉树构建一个「堆」
           self.minheap = [0]*(heapSize+1)
           # realSize用于记录「堆」的元素个数
           self.realSize = 0
   
       #  添加元素函数
       def add(self, element):
           self.realSize += 1
           # 如果「堆」中元素的个数大于一开始设定的数组的个数，则返回「Add too many elements」
           if self.realSize > self.heapSize:
               print("Add too many elements!")
               self.realSize -= 1
               return
           # 将添加的元素添加到数组中
           self.minheap[self.realSize] = element
           # 新增元素的索引位置
           index = self.realSize
           # 新增元素的父节点的索引位置
           # 注意，如果用数组表示完全二叉树，并且根结点存储在数组的索引1的位置的时候，任何一个节点的父节点索引位置为「该节点的索引位置/2」，任何一个节点的左孩子节点的索引位置为「该节点的索引位置*2」，任何一个节点的右孩子节点的索引位置为「该节点的索引位置*2+1」
           parent = index // 2
           # 当添加的元素小于父节点时，需要将父节点的值和新增元素的值交换
           while (self.minheap[index] < self.minheap[parent] and index > 1):
               self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
               index = parent
               parent = index // 2
       
       # 获取堆顶元素函数
       def peek(self):
           return self.minheap[1]
       
       # 删除堆顶元素函数
       def pop(self):
           # 如果当前「堆」的元素个数为0， 则返回「Don't have any element」
           if self.realSize < 1:
               print("Don't have any element!")
               return sys.maxsize
           else:
               # 当前「堆」中含有元素
               # self.realSize >= 1
               removeElement = self.minheap[1]
               # 将「堆」中的最后一个元素赋值给堆顶元素
               self.minheap[1] = self.minheap[self.realSize]
               self.realSize -= 1
               index = 1
               # 当删除的元素不是孩子节点时
               while (index < self.realSize and index <= self.realSize // 2):
                   # 被删除节点的左孩子节点
                   left = index * 2
                   # 被删除节点的右孩子节点
                   right = (index * 2) + 1
                   # 当删除节点的元素大于 左孩子节点或者右孩子节点，代表该元素的值大，此时需要将该元素与左、右孩子节点中最小的值进行交换
                   if (self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]):
                       if self.minheap[left] < self.minheap[right]:
                           self.minheap[left], self.minheap[index] = self.minheap[index], self.minheap[left]
                           index = left
                       else:
                           self.minheap[right], self.minheap[index] = self.minheap[index], self.minheap[right]
                           index = right
                   else:
                       break
               return removeElement
       
       # 返回「堆」的元素个数
       def size(self):
           return self.realSize
       
       def toString(self):
           print(self.minheap[1 : self.realSize+1])
   ```




3. **性能**：插入和删除最大/最小元素通常是 **O*(log*n)** 的时间复杂度。

   

#### **堆的分类**

堆有两种类型：**最大堆** 和 **最小堆**。

最大堆：**堆中每一个节点的值 都大于等于 其孩子节点的值。所以最大堆的特性是 堆顶元素（根节点）是堆中的最大值。**

最小堆：**堆中每一个节点的值 都小于等于 其孩子节点的值。所以最小堆的特性是 堆顶元素（根节点）是堆中的最小值。**

![image-20231024124548299](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231024124548299.png)



#### Python中的堆

Python的`heapq`模块提供了一组用于处理堆队列（也称为优先队列）的函数。特别地，`heapq`模块创建的是最小堆。以下是您提到的三个函数的详细介绍：

**1. `heapq.heapify(iterable)`**

这个函数用于将一个可迭代对象（比如列表）转换成一个有效的堆，即重新排列列表中的元素，使其满足堆的性质。堆的性质是指在任意索引`i`处的元素，其值都小于或等于索引`2*i + 1`和`2*i + 2`处的元素的值。

- **时间复杂度**：O(n)

- **参数**：一个可迭代对象（通常是列表）。

- **示例**：

  ```python
  import heapq
  
  nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
  heapq.heapify(nums)
  print(nums)  # 输出：[1, 1, 2, 3, 5, 9, 4, 6, 5]
  ```



**2. `heapq.heappushpop(heap, elem)`**

这个函数用于向堆中添加一个新元素并弹出堆顶元素，返回的是添加元素之前的堆顶元素。如果你想添加一个元素同时保持堆的大小不变，这个函数会比先调用`heappush()`再调用`heappop()`更高效。

- **时间复杂度**：O(log n)

- **参数**：

  - `heap`：一个已经是堆的列表。
  - `elem`：要添加到堆中的元素。

- **示例**：

  ```
  import heapq
  
  heap = [1, 3, 5, 7, 9]
  smallest = heapq.heappushpop(heap, 4)
  print(smallest)  # 输出：1
  print(heap)  # 输出：[3, 4, 5, 7, 9]
  ```



**3. `heapq.heappush(heap, elem)`**

这个函数用于向堆中添加一个新元素，同时保证堆的性质仍然满足。

- **时间复杂度**：O(log n)

- **参数**：

  - `heap`：一个已经是堆的列表。
  - `elem`：要添加到堆中的元素。

- **示例**：

  ```
  import heapq
  
  heap = [1, 3, 5, 7, 9]
  heapq.heappush(heap, 4)
  print(heap)  # 输出：[1, 3, 4, 7, 9, 5]
  ```



### 栈 vs 堆

- **存储方式**：栈通常是**连续的内存空间**，**堆则是动态分配**。

- **生命周期**：栈中的数据通常随函数的调用和返回而创建和销毁，而堆中的数据需要手动管理。

- **访问速度**：由于栈使用连续内存空间和局部性原理，通常访问速度更快。

- **灵活性**：堆由于是动态分配，更加灵活，但管理复杂。

- **应用场景**：栈适用于**需要快速、临时存储**的场景；堆则适用于需要**长时间存储或者快速找到最大/最小元素的场景**。

  



## 树

树是一种非线性数据结构，根据子节点数量可分为 「二叉树」 和 「多叉树」，最顶层的节点称为「根节点 root」。以二叉树为例，每个节点包含三个成员变量：「值 val」、「左子节点 left」、「右子节点 right」 。

### 二叉树

二叉树是一种树形数据结构，其中每个节点最多有两个子节点，通常分别称为“左子节点”和“右子节点”。二叉树的顶部节点称为“根节点”。

在编程语境中，一个简单的二叉树节点可以用以下结构定义：

Python

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

### 节点的深度（Depth）

在二叉树中，一个节点的“深度”定义为该节点到根节点的**最短路径上的边的数量**。根据这个定义，根节点的深度为0，其子节点的深度为1，依此类推。

例如，在以下二叉树中：

```
        A
       / \
      B   C
     / \
    D   E
```

- 节点A（根节点）的**深度是0**
- 节点B和C的**深度是1**
- 节点D和E的深度是2

### 节点的高度（Height）

一个节点的“高度”是从该节点到最远叶子节点的最长路径上的边的数量。在这个定义下，所有叶子节点的高度都是0。

还是以同样的例子为例：

```
        A
       / \
      B   C
     / \
    D   E
```

- 节点D和E（叶子节点）的高度是0
- 节点B的高度是1（到达叶子节点D或E需要经过一条边）
- 节点C的高度是0（它自己就是叶子节点）
- 节点A的高度是2（到达叶子节点D或E需要经过两条边）

### 遍历方式

在计算机科学中，前序遍历、中序遍历和后序遍历是用于遍历树结构（特别是二叉树）的三种主要方法。下面我会详细解释这三种遍历方法，并给出Python代码示例。

        A
       / \
      B   C
     / \
    D   E
**前序遍历（Preorder Traversal）**

前序遍历的顺序是：根节点 -> 左子树 -> 右子树。

```
def preorder_traversal(root):
    if root is None:
        return
    print(root.val, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)
    
    # 输出：['A', 'B', 'D', 'E', 'C']
```

**中序遍历（Inorder Traversal）**

中序遍历的顺序是：左子树 -> 根节点 -> 右子树。

```
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)
    
    # 输出：['D', 'B', 'E', 'A', 'C']
```

**后序遍历（Postorder Traversal）**

后序遍历的顺序是：左子树 -> 右子树 -> 根节点。

```
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=' ')
    
    # 输出：['D', 'E', 'B', 'C', 'A']
```

**示例代码**

下面是一个完整的Python代码示例，展示了如何定义一个简单的二叉树节点类，并对这个类的实例进行前序、中序和后序遍历。

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is None:
        return
    print(root.val, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=' ')

# 创建一个简单的二叉树
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 执行遍历
print("前序遍历：", end='')
preorder_traversal(root)
print("\n中序遍历：", end='')
inorder_traversal(root)
print("\n后序遍历：", end='')
postorder_traversal(root)
```

### 搜索 

根据BST的特性，对于每个节点：

如果目标值等于节点的值，则返回节点；
如果目标值小于节点的值，则继续在左子树中搜索；
如果目标值大于节点的值，则继续在右子树中搜索。

![image-20231027164631889](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231027164631889.png)

### 插入

二叉搜索树中的另一个常见操作是插入一个新节点。有许多不同的方法去插入新节点，这篇文章中，我们只讨论一种使整体操作变化最小的经典方法。 它的主要思想是为目标节点找出合适的叶节点位置，然后将该节点作为叶节点插入。 因此，搜索将成为插入的起始。

与搜索操作类似，对于每个节点，我们将：

根据节点值与目标节点值的关系，搜索左子树或右子树；
重复步骤 1 直到到达外部节点；
根据节点的值与目标节点的值的关系，将新节点添加为其左侧或右侧的子节点。
这样，我们就可以添加一个新的节点并依旧维持二叉搜索树的性质。

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231027170558461.png" alt="image-20231027170558461" style="zoom:50%;" />



### 删除

删除要比我们前面提到过的两种操作复杂许多。有许多不同的删除节点的方法，这篇文章中，我们只讨论一种使整体操作变化最小的方法。我们的方案是用一个合适的子节点来替换要删除的目标节点。根据其子节点的个数，我们需考虑以下三种情况：

1. 如果目标节点没有子节点，我们可以直接移除该目标节点。
2. 如果目标节只有一个子节点，我们可以用其子节点作为替换。
3. 如果目标节点有两个子节点，我们需要用其中序后继节点或者前驱节点来替换，再删除该目标节点。

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231027172446938.png" alt="image-20231027172446938" style="zoom:50%;" />





### 优点

二叉搜索树的有优点是，即便在最坏的情况下，也允许你在**O(n)的时间复杂度**内执行所有的搜索、插入、删除操作。

通常来说，如果你想有序地存储数据或者**需要同时执行搜索、插入、删除等多步操作，**二叉搜索树这个数据结构是一个很好的选择。

> 问题描述：设计一个类，求一个数据流中第k大的数。
>
> 一个很显而易见的解法是，先将数组降序排列好，然后返回数组中第k个数。
>
> 但这个解法的缺点在于，为了在O(1)时间内执行搜索操作，每次插入一个新值都需要重新排列元素的位置。从而使得插入操作的解法平均时间复杂度变为O(N)。因此，算法总时间复杂度会变为O(N^2)。
>
> 鉴于我们同时需要插入和搜索操作，为什么不考虑使用一个二叉搜索树结构存储数据呢？
>
> 我们知道，对于二叉搜索树的每个节点来说，它的左子树上所有结点的值均小于它的根结点的值，右子树上所有结点的值均大于它的根结点的值。
>
> 换言之，对于二叉搜索树的每个节点来说，若其左子树共有m个节点，那么该节点是组成二叉搜索树的有序数组中第m + 1个值。





### 平衡二叉树

平衡二叉树（Balanced Binary Tree）是一种特别的二叉树，其设计初衷是为了解决普通二叉搜索树在极端情况下可能出现的效率问题（比如，当所有节点都在一侧时，二叉搜索树退化为链表）。

**定义**

平衡二叉树必须满足两个条件：

1. **每个节点的左子树和右子树的高度差（称为平衡因子）不得超过一个给定的常数（通常为 1）**。
2. **每个节点的左子树和右子树也都必须是平衡二叉树**。

**判断是否为平衡二叉树**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def height(root):
        if not root:
            return 0
        left_height = height(root.left)
        right_height = height(root.right)
        
        # 如果子树是不平衡的，则提前停止
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1

    return height(root) != -1
```



## 图

图是一种非线性数据结构，由「节点（顶点）**vertex**」和「边 **edge**」组成，每条边连接一对顶点。根据边的方向有无，图可分为「有向图」和「无向图」。本文 以无向图为例 开展介绍。

如下图所示，此无向图的 顶点 和 边 集合分别为：

- 顶点集合： vertices = {1, 2, 3, 4, 5}
- 边集合： edges = {(1, 2), (1, 3), (1, 4), (1, 5), (2, 4), (3, 5), (4, 5)}

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231028230151220.png" alt="image-20231028230151220" style="zoom: 33%;" />

## 散列表

散列表是一种非线性数据结构，通过利用 Hash 函数将指定的**「键 key」映射至对应的「值 value」**，以实现高效的元素查找。

设想一个简单场景：小力、小特、小扣的学号分别为 10001, 10002, 10003 。
现需求从「姓名」查找「学号」。

则可通过建立姓名为 key ，学号为 value 的散列表实现此需求，代码如下：

```java
// 初始化散列表
Map<String, Integer> dic = new HashMap<>();

// 添加 key -> value 键值对
dic.put("小力", 10001);
dic.put("小特", 10002);
dic.put("小扣", 10003);

// 从姓名查找学号
dic.get("小力"); // -> 10001
dic.get("小特"); // -> 10002
dic.get("小扣"); // -> 10003
```

```python
# 初始化散列表
dic = {}

# 添加 key -> value 键值对
dic["小力"] = 10001
dic["小特"] = 10002
dic["小扣"] = 10003

# 从姓名查找学号
dic["小力"] # -> 10001
dic["小特"] # -> 10002
dic["小扣"] # -> 10003
```



# 算法复杂度

### 时间复杂度

时间复杂度（Time Complexity）描述的是执行算法所需要的计算工作量，通常是随着输入大小的增加而增加。常用的表示方法包括：

- **常数时间（O(1)）**：无论输入多大，算法所需时间都是常数。

- **对数时间（O(log n)）**：每一步算法都会大幅减少问题的规模。二分查找是典型的对数时间复杂度算法。

- **线性时间（O(n)）**：算法的运行时间与输入规模成正比。例如，简单搜索算法通常具有线性时间复杂度。

- **线性对数时间（O(n log n)）**：许多高效的排序算法，如**归并排序、快速排序**等，具有线性对数时间复杂度。

- **平方时间（O(n^2)）或多项式时间（O(n^k)）**：嵌套循环或递归算法通常具有这种复杂度。例如，冒泡排序具有平方时间复杂度。

- **指数时间（O(2^n)）**：某些**递归**算法，如计算斐波那契数列的暴力解法，具有指数时间复杂度。

- **阶乘时间（O(n!)）**：**旅行商问题**的暴力解法就是一个阶乘时间复杂度的例子。

  

**示例 1：常数时间复杂度 O(1)**

```
def constant_example(arr):
    return arr[0] if arr else None

# 调用
result = constant_example([1, 2, 3])
```

无论数组 `arr` 的大小如何，这个函数都只返回数组的第一个元素，因此其时间复杂度为 O(1)。

**示例 2：线性时间复杂度 O(n)**

```
def linear_example(arr):
    for item in arr:
        print(item)

# 调用
linear_example([1, 2, 3, 4])
```

这个函数遍历整个数组并打印每个元素。因此，其时间复杂度是 O(n)，其中 n 是数组的长度。

**示例 3：对数时间复杂度 O(log n)**

```
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 调用
result = binary_search([1, 2, 3, 4, 5, 6], 3)
```

二分查找每次迭代都会将搜索范围减小一半，因此其时间复杂度是 O(log n)。

**示例 4：线性对数时间复杂度 O(n log n)**

```
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

# 调用
result = merge_sort([38, 27, 43, 3, 9, 82, 10])
```

归并排序的时间复杂度是 O(n log n)，因为它每次都把问题规模减小到一半（log n），并且每次都需要处理 n 个元素。



**示例 5：平方时间复杂度 O(n^2)**

```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 调用
bubble_sort([64, 34, 25, 12, 22, 11, 90])
```

在这个冒泡排序的示例中，有两个嵌套的循环，每个循环都遍历数组一次。因此，时间复杂度是 O(n^2)。

**示例 6：指数时间复杂度 O(2^n)**

```
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 调用
print(fibonacci(10))
```



#### 特殊的内置函数

**Python**

- `list.sort()` 或 `sorted()`: 内置排序通常具有 O(n log n) 的时间复杂度。
- `list.append()`：平均时间复杂度为 O(1)，但如果涉及到动态数组的扩容，则可能会达到 O(n)。
- `list.pop(0)`: 删除列表的第一个元素需要 O(n) 的时间。

**Java**

- **集合操作**

1. **ArrayList.remove(int index)**：删除指定索引处的元素需要 O(n) 的时间，因为这涉及到移动所有后续元素。
2. **LinkedList.get(int index)**：在 LinkedList 中通过索引查找一个元素需要 O(n) 的时间。

- **字符串操作**

1. **String.concat(String str)**：字符串连接在 Java 中通常需要 O(n+m) 的时间，其中 n 和 m 是两个字符串的长度。

2. **String.substring(int beginIndex, int endIndex)**：这个操作在 Java 6 以前是 O(1)，但在更高版本中由于改变了内部实现，现在是 O(n)。

   

### 空间复杂度

空间复杂度（Space Complexity）描述的是算法在运行过程中临时占用存储空间的大小。常见的空间复杂度包括：

- **常数空间（O(1)）**：算法使用固定量的额外内存空间。
- **线性空间（O(n)）**：动态数组或列表可能需要线性大小的额外空间。

空间复杂度涉及的空间类型有：

- 输入空间： 存储输入数据所需的空间大小；
- 暂存空间： 算法运行过程中，存储所有中间变量和对象等数据所需的空间大小；
- 输出空间： 算法运行返回时，存储输出数据所需的空间大小；

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231029014703649.png" alt="image-20231029014703649" style="zoom:50%;" />

- **Python 代码示例**

**常数空间复杂度 O(1)**

```
def find_max(arr):
    max_val = float('-inf')
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# 调用
print(find_max([1, 2, 3, 4]))
```

这个函数使用了一个额外的变量 `max_val` 来存储最大值，因此其空间复杂度为 O(1)。

**线性空间复杂度 O(n)**

```
def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# 调用
print(reverse_array([1, 2, 3, 4]))
```

这个函数创建了一个新数组，其长度与输入数组相同，因此空间复杂度为 O(n)。

- **Java 代码示例**

**常数空间复杂度 O(1)**

```
public class Main {
    public static int findMin(int[] arr) {
        int minVal = Integer.MAX_VALUE;
        for(int num : arr) {
            if(num < minVal) {
                minVal = num;
            }
        }
        return minVal;
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 4, 1, 5, 9};
        System.out.println(findMin(arr));
    }
}
```

这个 Java 函数同样只使用了一个额外的变量来存储最小值，因此空间复杂度也是 O(1)。

**线性空间复杂度 O(n)**

```
public class Main {
    public static int[] duplicateArray(int[] arr) {
        int[] duplicatedArr = new int[arr.length];
        for(int i = 0; i < arr.length; i++) {
            duplicatedArr[i] = arr[i];
        }
        return duplicatedArr;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int[] duplicatedArr = duplicateArray(arr);
        for(int num : duplicatedArr) {
            System.out.print(num + " ");
        }
    }
}
```



- **常数 O(1) ：**

  普通常量、变量、对象、元素数量与输入数据大小 N 无关的集合，皆使用常数大小的空间。

Python

```Python
def algorithm(N):
    num = 0
    nums = [0] * 10000
    node = Node(0)
    dic = { 0: '0' }
```

如以下代码所示，虽然函数 test() 调用了 N 次，但每轮调用后 test() 已返回，无累计栈帧空间使用，因此空间复杂度仍为 O(1) 。

Python

```Python
def algorithm(N):
    for _ in range(N):
        test()
```

线性 O(N) ：
元素数量与 N 呈线性关系的任意类型集合（常见于一维数组、链表、哈希表等），皆使用线性大小的空间。

Python

```python
def algorithm(N):
    nums_1 = [0] * N
    nums_2 = [0] * (N // 2)
    nodes = [Node(i) for i in range(N)]

    dic = {}
    for i in range(N):
        dic[i] = str(i)
```

如下图与代码所示，此递归调用期间，会同时存在 N 个未返回的 algorithm() 函数，因此使用 **O(N)** 大小的栈帧空间。

Python

```Python
def algorithm(N):
    if N <= 1: return 1
    return algorithm(N - 1) + 1
```

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231029015711413.png" alt="image-20231029015711413" style="zoom:50%;" />

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231029020645535.png" alt="image-20231029020645535" style="zoom: 67%;" />

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231029020715109.png" alt="image-20231029020715109" style="zoom:67%;" />

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231029020734544.png" alt="image-20231029020734544" style="zoom:67%;" />