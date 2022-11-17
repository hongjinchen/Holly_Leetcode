# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxLevel = -1
        result = 0

        # 深度遍历
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return
            if level > maxLevel:
                level = maxLevel
                result = node.val
            elif level == maxLevel:
                result += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result
