# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals = sorted(intervals)
        return self.merge(intervals)

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        answer = []

        intervals = sorted(intervals)
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


# # 排序 + 区间合并
if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
