# 中信技术测试 -题目一
import math
# Ø题目一：小组成员反转排队。（50min）
# 题目描述：为增强新小组成员默契程度，现将小组成员编号后排列；如果现有小组成员数为k，则由组长随机指定一个数字n（1<= n <=k），
# 组员接收到指令后，前n个组员反转排列，然后再让前n/3个（向上取整）组员反转排列；
# 接着组长再指定一个数字m(1<= m <=k），后m个队员也反转站立，然后再后m/3个（向上取整）队员页反转排列。
# 请根据初始的队列和组长给出的n，m指令，给出最后的队列编号。
# 输入：数字n，数字m，队列可在代码中指定，人数不少于10
# 输出：反转排队后的序列
# 时间限制：无限制。
# 样例1：输入：5,3	[1,2,3,4,5,6,7,8,9,10,11]
# 输出：[4,5,3,2,1,6,7,8,11,10,9]
# 样例2：输入：6,8	[1,2,3,4,5,6,7,8,9,10,11,12]
# 输出：[5,6,4,3,12,11,10,9,8,2,1,7]

def reverse_queue(n, m, queue):
    # 异常判断
    if n<1 or n>len(queue) or m<1 or m>len(queue):
        return "n,m 必须在范围内"
    
    if len(queue)==1:
        return queue

    # (前)
    # 先反转数字n
    n_reversed = queue[:n][::-1]
    # 向上取整--math.ceil(n/3)

    # 反转前n/3个组员
    n_reversed[:math.ceil(n/3)] = n_reversed[:math.ceil(n/3)][::-1]

    # 将新反转的代码添加到原有的queue里
    queue=n_reversed+queue[n:]

    # (中)
    # 保留n-m中间的，因为这部分内容不会进行修改
    middle_segment = queue[n:-m]
    # print("mid",middle_segment)

    # (后)
    # 反转后m个队员
    m_reversed = queue[-m:][::-1]
    # 后m/3个队员页反转排列
    m_reversed[-math.ceil(m/3):] = m_reversed[-math.ceil(m/3):][::-1]

    if n+m>len(queue):
        queue=queue[:len(queue)-m]+m_reversed
    else:
        queue=queue[:n]+middle_segment+m_reversed
    return queue

# Examples
example1 = reverse_queue(5, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
example2 = reverse_queue(6, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# example3 = reverse_queue(1, 1, [1])
example3 = reverse_queue(7, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

print(example1)
print(example2)
print(example3)