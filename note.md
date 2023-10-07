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







# 排序问题



## 冒泡排序

[75. 颜色分类](https://leetcode.cn/problems/sort-colors/)



# 回溯算法和DFS

回溯算法是一种用于找到所有（或某些）可能解决方案的算法，特别是在涉及约束满足问题（Constraint Satisfaction Problems，CSP）的情况下。回溯算法的核心思想是从问题的可能解决方案的空间树中，按照深度优先搜索（DFS）的策略，从根节点出发遍历解空间树。