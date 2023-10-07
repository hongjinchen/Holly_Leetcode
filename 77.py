# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

# 你可以按 任何顺序 返回答案。

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # return list(itertools.combinations(range(1, n+1), k))
        # 调用包解决问题

        # 回溯法
        res = []
        def backtrack(start=1, track=[]):
            if len(track) == k:
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
