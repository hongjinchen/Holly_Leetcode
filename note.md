

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

### 时间复杂度

- 最好情况*O*(1)（目标元素就在集合的中间位置）
- 平均和最坏情况：O(logn)



### 相关问题

[33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

[34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)



# 动态规划





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

```
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

使用memo（记忆化）的核心思想是保存已经计算过的子问题的解，以便在将来需要时可以直接使用，从而避免重复计算。这在递归算法中尤其有效，因为递归算法往往会多次计算相同的子问题。



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

致力于构建和优化四种不同类型的情感分类器，包括两个传统的机器学习模型（朴素贝叶斯和支持向量机）和两个神经网络模型（LSTM和GRU）。项目开始于对Semeval 2017提供的数据集进行初步分析，识别出类别不平衡等问题，并对数据进行了一系列预处理步骤，如文本清洗和词形还原。
继续开发了用于特征提取的多种方法，包括TF-IDF和词嵌入，以及尝试了各种不同的优化算法，如Adam和SGD。在模型训练阶段，利用交叉验证和网格搜索来调整超参数，并使用了不同的评估指标，如准确率和F1分数，来比较四种模型的性能。

朴素贝叶斯和支持向量机在一些基线测试中表现出色，但在处理更复杂的情感模式时遇到了局限性。与此同时，LSTM和GRU神经网络模型展示了更高的准确性和灵活性，尤其是在捕捉文本中长距离依赖关系方面。

经过多轮实验和调优，最终选择了GRU模型作为最优解，该模型在测试集上达到了最高的F1分数。



# 排序问题



## 冒泡排序

[75. 颜色分类](https://leetcode.cn/problems/sort-colors/)



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
   
     ```
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

### 栈（Stack）

1. **定义**：栈是一种后进先出（LIFO，Last-In-First-Out）的数据结构。
2. **操作**：主要有两种基本操作——压栈（push）和弹栈（pop）。
3. **应用**：函数调用、表达式求值、深度优先搜索等。
4. **存储**：通常使用数组或链表来实现。
5. **性能**：压栈和弹栈操作通常是 O(1) 的时间复杂度。

**示例代码（Python）**

```
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
```

### 堆（Heap）

1. **定义**：堆是一种特殊的完全二叉树，满足堆的性质（最大堆或最小堆）。
2. **操作**：插入元素、删除最大/最小元素等。
3. **应用**：优先队列、堆排序、图算法（如 Dijkstra 算法）等。
4. **存储**：通常使用数组来实现。
5. **性能**：插入和删除最大/最小元素通常是 �(log⁡�)*O*(log*n*) 的时间复杂度。

**示例代码（Python，最小堆）**

```
import heapq

# 初始化一个空堆
heap = []

# 插入元素
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)

# 删除并返回最小元素
min_val = heapq.heappop(heap)  # 返回 1
```

### 栈 vs 堆

- **存储方式**：栈通常是连续的内存空间，堆则是动态分配。
- **生命周期**：栈中的数据通常随函数的调用和返回而创建和销毁，而堆中的数据需要手动管理。
- **访问速度**：由于栈使用连续内存空间和局部性原理，通常访问速度更快。
- **灵活性**：堆由于是动态分配，更加灵活，但管理复杂。
- **应用场景**：栈适用于需要快速、临时存储的场景；堆则适用于需要长时间存储或者快速找到最大/最小元素的场景。



## 链表

### 相关题目

[82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/)

[86. 分隔链表](https://leetcode.cn/problems/partition-list/)

## 二叉树

### 平衡二叉树

平衡二叉树（Balanced Binary Tree）是一种特别的二叉树，其设计初衷是为了解决普通二叉搜索树在极端情况下可能出现的效率问题（比如，当所有节点都在一侧时，二叉搜索树退化为链表）。

**定义**

平衡二叉树必须满足两个条件：

1. **每个节点的左子树和右子树的高度差（称为平衡因子）不得超过一个给定的常数（通常为 1）**。
2. **每个节点的左子树和右子树也都必须是平衡二叉树**。

**判断是否为平衡二叉树**

```
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



# 双指针法

## 相关题目

### 合并有序数组

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



### 回文串判断 

其中一个指针从字符串开始处开始移动，另一个从字符串末尾开始移动。两个指针都只会经过一半的字符串，因此该算法的时间复杂度是 O(n/2)，即 O(n)。

```
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



