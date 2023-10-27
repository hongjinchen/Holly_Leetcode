# 给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

# 输入：root = [4,2,7,1,3], val = 5
# 输出：[4,2,7,1,3,5]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        def helper(root,val):

            if root==None:
                return TreeNode(val)
            if root.val<val:
                root.right=helper(root.right,val)
            elif root.val>val:
                root.left=helper(root.left,val)
            return root
        
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

if __name__=="__main__":
    solution=Solution()
    root_list = [4,2,7,1,3]
    val = 5
    root=build_tree_from_list(root_list)
    root=solution.insertIntoBST(root,val)
