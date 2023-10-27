# 给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

# 示例 1:
# 输入：root = [4,2,7,1,3], val = 2
# 输出：[2,1,3]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(root,val):
            if root is None:
                return None
            if root.val==val:
                return root
            elif root.val>val:
                return helper(root.left,val)
            elif root.val<val:
                return helper(root.right,val)
        return helper(root,val)
       

# 构建二叉树
def build_tree_from_list(lst: list[int]) -> TreeNode:
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while i < len(lst):
        current = queue.pop(0)
        
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        
        i += 1
        if i >= len(lst):
            break
        
        if lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        
        i += 1
    
    return root

def preorder_traversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

if __name__=="__main__":
    solution=Solution()
    root_list = [4,2,7,1,3]
    val = 5

    root=build_tree_from_list(root_list)

    answer=solution.searchBST(root,val)
    # 遍历
    print(preorder_traversal(answer))

