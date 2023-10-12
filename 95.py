# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        # DFS
        if n == 0:
            return []
        if n == 1:
            return [[TreeNode(1)]]

        self.res = []
        number_list = [i for i in range(1, n+1)]

        # 将从1到n的数字在一个list中，然后进行DFS，每次DFS都会将当前的数字作为根节点
        # 然后选择左子树和右子树，递归进行，直到list中数字为空，如果左子树或者右子树为空则结束当前的递归，并且将当前的数添加到结果中
        # 遍历每一个可能的根节点
        for number in number_list:
            head = TreeNode(number)
            new_list = number_list.copy()
            new_list.remove(number)
            self.DFS(new_list, head, head)

        return self.res
    def DFS(self, number_list, current_node, head):
        if len(number_list) == 0:
            self.res.append(self.copyTree(head))
            return

        for number in number_list:
            new_list = number_list.copy()
            new_list.remove(number)
          # 二叉搜索树（Binary Search Tree, BST）的定义：即对于任何节点，其左子树的所有元素都应小于该节点，而右子树的所有元素都应大于该节点。
            if number < current_node.val:
                current_node.left = TreeNode(number)
                self.DFS(new_list, current_node.left, head)
                current_node.left = None  # 回溯
            else:
                current_node.right = TreeNode(number)
                self.DFS(new_list, current_node.right, head)
                current_node.right = None  # 回溯


    def copyTree(self, node):
        if not node:
            return None
        new_node = TreeNode(node.val)
        new_node.left = self.copyTree(node.left)
        new_node.right = self.copyTree(node.right)
        return new_node


if __name__ == "__main__":
    solution = Solution()
    n = 3
    all_trees = solution.generateTrees(n)

    def preorder_traversal(root):
        if root is None:
            return []
        return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

    for tree in all_trees:
        print(preorder_traversal(tree))
