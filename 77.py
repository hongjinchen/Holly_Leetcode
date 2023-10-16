# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

# 你可以按 任何顺序 返回答案。

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # return list(itertools.combinations(range(1, n+1), k))
        # 调用包解决问题

        # 回溯法
        # 递归就可以用于解决多层嵌套循环的问题了
        res = []
        def backtrack(start=1, track=[]):
            if len(track) == k:
                # 回溯函数终止条件
                # 什么时候到达所谓的叶子节点了呢？
                # path这个数组的大小如果达到k，说明我们找到了一个子集大小为k的组合了，在图中path存的就是根节点到叶子节点的路径。
                res.append(track[:])
                return
            for i in range(start, n+1):
                track.append(i)
                backtrack(i+1, track)
                track.pop()
        
        backtrack()
        return res

    
if __name__ == "__main__":
    s = Solution()
    print(s.combine(4,2))
