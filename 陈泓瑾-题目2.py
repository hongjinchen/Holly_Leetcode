# Ø题目二：互联网大会会议统筹。（70min）
# 任务安排系统，为了实现最优的时间安排-用最少的天数统筹完所有的会议
# 会议室：1个
# 一天：8个小时
# 会议时长单位：0.5小时
# 规则：一天内相同类型的会议必须安排在一起连续召开

# 输入：输入多个string，以空格分隔，每3个string描述一个会议安排，表示会议名、会议时长和会议类型，
# 输出：按照时间顺序打印会议召开的顺序，并标明不同的日期
# 样例1：输入：[‘conference1’, 1.5, ‘A’, ‘conference2’, 1, ‘B’, ‘conference3’, 2.5, ‘A’]，
# 输出
# Day 1:
# ‘conference1’, 1.5, ‘A’
# ‘conference3’, 2.5, ‘A’
# ‘conference2’, 1, ‘B’
#  需要先解析输入的代码

# 样例2：输入：[‘conference1’, 4.5, ‘A’, ‘conference2’, 3, ‘B’, ‘conference4’, 2.5, ‘C’, ‘conference3’, 2.5, ‘A’, ‘conference5’, 1.5, ‘C’]
# 输出
# Day 1:
# ‘conference1’, 4.5, ‘A’
# ‘conference3’, 2.5, ‘A’
# Day 2:
# ‘conference2’, 3, ‘B’
# ‘conference4’, 2.5, ‘C’
# ‘conference5’, 1.5, ‘C’

input_string="conference1 1.5 A conference2 1 B conference2 2.5 A"
# input_string=input("")
# 分割字符串
strings = input_string.split()
#strings example: ['conference1', '4.5', 'A', 'conference2', '3', 'B', 'conference4', '2.5', 'C', 'conference3', '2.5', 'A', 'conference5', '1.5', 'C']

# 组织和解析会议信息,以三个为一组--会议名、会议时长和会议类型
meetings = []
for i in range(0, len(strings), 3):
    meeting_name = strings[i]
    meeting_duration = strings[i + 1]
    meeting_type = strings[i + 2]

    meetings.append({
            "name": meeting_name,
            "duration": meeting_duration,
            "type": meeting_type
        })
# 以这样的格式去储存信息：{'name': 'conference1', 'duration': '4.5', 'type': 'A'}

# # 首先考虑一共有多少个类型的会议，并且计算每个类型的会议总时长
# meeting_durations = {}
# for conference in meetings:
#     if conference["type"] not in meeting_durations:
#         meeting_durations[conference["type"]] = float(conference["duration"])
#     else:
#         meeting_durations[conference["type"]] += float(conference["duration"])

# 对于每种类型的会议，可能存在需要开很多天的情况，
# 对每种类型的会议，根据其总时长来分配需要的天数。
# 每种类型的会议应该连续安排，直到其总时长被安排完毕。
# 如果某一天的剩余时间不足以安排当前类型的所有剩余会议，
# 就将该类型的剩余会议推迟到下一天。

schedule = []

for meeting in meetings:
    remaining_duration = float(meeting["duration"])
    meeting_type = meeting["type"]
    # print(meeting["name"])
    # 遍历日程表，先尝试在有空余时间的相同类型的天中安排会议(针对同一个会议数量较多，总时长较长的情况)
    is_added_existing_day = False
    for day in schedule:
        # if day["remaining"] >= remaining_duration and day["type"] == meeting_type:
        if day["remaining"] >= remaining_duration:
            day["meetings"].append((meeting["name"], remaining_duration))
            day["remaining"] -= remaining_duration
            is_added_existing_day = True
            break

    # 如果没有找到合适的天（type），或者当天的剩余时间不足，开启新的一天会议
    if not is_added_existing_day:
        new_day = {"meetings": [(meeting["name"], float(remaining_duration))], "remaining": 8.0 - float(remaining_duration), "type": meeting_type}
        schedule.append(new_day)

# 输出
output = []
day_number = 1
for day in schedule:
    # 为了添加参数使用了f
    output.append(f"Day {day_number}:")
    for meeting in day["meetings"]:
        output.append(f"{meeting[0]}, {meeting[1]}, '{day['type']}'")
    day_number += 1

# '\'是转义字符，'\n'在字符串中表示产生一个换行操作.join()的用法是将括号中的参数（本例是tds列表）中的各项进行连接，返回一个字符串。
output="\n".join(output)
print(output)