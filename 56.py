# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        answer = []

        intervals=sorted(intervals)
        for interval in intervals:
            if len(answer) == 0:
                answer.append(interval)
            else:
                for index in range(len(answer)):
                    interval_answer = answer[index]
                    if interval[0] <= interval_answer[1]:
                        interval_answer[1] = max(
                            interval_answer[1], interval[1])
                        interval_answer[0] = min(
                            interval_answer[0], interval[0])
                        answer[index] = interval_answer
                        break
                else:
                    answer.append(interval)
        
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,4],[0,0]]))

    # [[1, 3], [2, 6], [8, 10], [15, 18]]
    # 如果interval[1]大于其他的interval[0]，那么就合并，并且获得两个interval的最大值和最小值，进行组合
