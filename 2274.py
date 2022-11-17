from itertools import pairwise



bottom = 6
top = 8
special = [7,6,8]
# max_value=0
# floor=0
# for i in range(bottom,top+1,1):
#     if i not in special:
#         floor=floor+1
#         if floor>max_value:
#             max_value=floor
#     else:
#         floor=0
# print(max_value)
# 上面的解法需要优化，因为会超出时间限制，如果数很大
special.append(bottom-1)
special.append(top+1)
special=sorted(special)
print(max(y - x - 1 for x, y in pairwise(special)))