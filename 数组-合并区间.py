# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals)==1 or 0:
            return intervals
        intervals=sorted(intervals,key=lambda x:x[0])
        result=[intervals[0]]
        for item in intervals:
            if item[-1]<=result[-1][-1]:
                continue
            elif item[0]<=result[-1][-1]:
                result[-1][-1]=item[-1]
            else:
                result.append(item)
        return result



if __name__=="__main__":
    s=Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))