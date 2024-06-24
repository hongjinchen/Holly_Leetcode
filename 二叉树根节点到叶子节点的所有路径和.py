# 二叉树根节点到叶子节点的所有路径和是指将二叉树中从根节点到任意一个叶子节点的路径上的节点值累加起来，然后对所有这些路径和求总和

# 递归

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root):
    # 辅助函数，用于递归计算路径和
    def dfs(node):
        if not node:  # 基本情况：如果节点为空，返回0
            return 0
        
        if not node.left and not node.right:  # 如果是叶子节点，返回当前路径和
            return node.val
        
        # 递归计算左右子树的路径和
        return node.val+dfs(node.left) + dfs(node.right)
    
    return dfs(root)  # 从根节点开始，初始路径和为0

# 示例
# 构建一个简单的二叉树
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# 计算根节点到叶子节点的所有路径和
print(sumRootToLeaf(root))  # 输出 6 (1+2 + 1+3)