# 统计字符频次：遍历字符串，使用哈希表（如Python中的字典）记录每个字符的出现次数。
# 排序频次：将记录的频次转换为一个列表，并根据频次对列表进行排序（降序）。
# 选择最高和第二高：从排序后的列表中选择频次最高的字符作为出现最多的字符，选择频次第二高的字符作为出现第二多的字符。

def find_most_frequent_chars(s):
    # 统计字符频次
    freq_map = {}
    for char in s:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    
    # 将频次转换为列表并排序
    freq_list = [(char, count) for char, count in freq_map.items()]
    freq_list.sort(key=lambda x: x[1], reverse=True)
    
    # 获取出现最多和第二多的字符
    if len(freq_list) > 0:
        most_frequent = freq_list[0][0]
    if len(freq_list) > 1:
        second_most_frequent = freq_list[1][0]
    
    return most_frequent, second_most_frequent

# 示例
s = "aabbbccccdddd"
most_frequent, second_most_frequent = find_most_frequent_chars(s)
print(f"出现最多的字符是: {most_frequent}")
print(f"出现第二多的字符是: {second_most_frequent}")