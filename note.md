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

# 分治法





# 递归

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



# 数据结构

## 链表

### 相关题目

[82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/)

[86. 分隔链表](https://leetcode.cn/problems/partition-list/)





# 面试题目

## 合并有序数组

### 方法1：双指针法

1. 使用两个指针分别遍历两个有序数组。
2. 比较两个指针指向的元素，将较小的元素添加到结果数组中，并将对应的指针向前移动。
3. 如果一个数组遍历完了，将另一个数组剩余的元素添加到结果数组中。

