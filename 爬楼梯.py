# 问题描述：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？

def climb_stairs(n, memo={}):
    if n in memo:
        # 检查 memo 字典中是否已经有了 n 级台阶的解法。如果有，直接返回这个值。
        return memo[n]
    if n == 1:
        # 如果台阶数为 1，只有一种爬法，即直接爬一级。
        return 1
    if n == 2:
        # 如果台阶数为 2，有两种爬法：先爬一级再爬一级，或者直接爬两级。
        return 2
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]
# 如果找到了，就返回存储在 memo 中的值。

# 测试
print(climb_stairs(5))  # 输出 8