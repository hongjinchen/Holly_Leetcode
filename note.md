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



[46. 全排列](https://leetcode.cn/problems/permutations/)

[47. 全排列 II](https://leetcode.cn/problems/permutations-ii/)