# 组合问题可以抽象为树形结构
# 该算法为回溯算法
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        # 先进行排序，可以减少计算量
        ans = []
        def find(s,use,remain):
            for i in range(s,len(candidates)):
                c = candidates[i]
                if i>s and candidates[i-1]==candidates[i]:
                    continue
                if c == remain:
                    ans.append(use + [c])
                    return      
                # 回退
                if c < remain:
                    find(i+1,use + [c], remain - c)
                if c > remain:
                    return
                # 回退
        find(0,[], target)
        return ans

if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    new_solu = Solution()
    print(new_solu.combinationSum2(candidates, target))
