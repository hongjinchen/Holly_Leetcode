# 要生成n对括号的所有有效排列，可以使用递归的方法。在递归过程中，维护两个计数器：一个用于左括号的数量left，另一个用于右括号的数量right。基本思想是：

# 只有当左括号的数量少于n时，我们才添加一个左括号。
# 只有当右括号的数量少于左括号的数量时，我们才添加一个右括号。
# 当左括号和右括号的数量都达到n时，我们得到了一个有效的排列。

def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result

# 使用示例
n = 3
print(generate_parentheses(n))