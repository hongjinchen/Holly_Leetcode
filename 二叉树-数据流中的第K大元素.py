# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
# 请实现 KthLargest 类：
# KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
# int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
# 示例：
# 输入：
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# 输出：
# [null, 4, 5, 5, 8, 8]
# 解释：
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums=nums
        self.k=k

        self.nums.sort(reverse=True)
        while len(self.nums) > k:
            self.nums.pop()

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        while len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]
    
# 使用最小堆：可以使用一个容量为k的最小堆（min-heap）来保存最大的k个元素。这样，堆顶就是第k大的元素。Python中的heapq库可以很方便地实现最小堆。

# 添加元素时的效率：使用最小堆，你可以在O(log k)的时间内添加一个新元素，同时仍然能在O(1)的时间内获取第k大的元素。
    # def __init__(self, k: int, nums: list[int]):
    #     self.k = k
    #     self.min_heap = nums[:k]
    #     heapq.heapify(self.min_heap)
        
    #     for num in nums[k:]:
    #         if num > self.min_heap[0]:
    #             heapq.heappushpop(self.min_heap, num)

    # def add(self, val: int) -> int:
    #     if len(self.min_heap) < self.k:
    #         heapq.heappush(self.min_heap, val)
    #     elif val > self.min_heap[0]:
    #         heapq.heappushpop(self.min_heap, val)
        
    #     return self.min_heap[0]

