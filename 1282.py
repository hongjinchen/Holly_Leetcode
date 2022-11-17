groupSizes = [2, 1, 3, 3, 3, 2]
group = {}
index = 0
answer = []
for item in groupSizes:
    if item in group:
        group[item].append(index)
    else:
        group[item] = [index]
    index = index + 1
for items in group:
    if len(group[items]) == items:
        answer.append(group[items])
    else:
        new_list = [
            group[items][i:i + items]
            for i in range(0, len(group[items]), items)
        ]
        for item in new_list:
            answer.append(item)

print(answer)

## 哈希表
a = dict()
b = {}
c = {'a': 1, 'b': 2, 'b': '3'}  # 冒号左边是key，右边是value，由于存在重复的b，最后剩下右边的'b':3
##字典的初始化
print (c['a'])
##访问字典中的value
c['a'] = 0 # 将原来映射的1变为0
c['c'] = 4 # 添加新的键值对
##修改字典
del c['a'] #删除key为a的键值对
c.clear #清除字典c中所有的键值对
del c #直接删除字典c
##删除字典元素