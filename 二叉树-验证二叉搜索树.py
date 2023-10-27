# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 输入：root = [2,1,3]
# 输出：true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
# 判断二叉树是否是正确的
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def helper(root,lower,higher):
            
            if root is None:
                return True
            
            val=root.val

            if val>lower and val<higher:
                return (helper(root.left,lower,val) and helper(root.right,val,higher))
            else:
                return False
        return helper(root,float('-inf'),float('inf'))

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
    head=TreeNode()
    node_list = [2,2,2]
    root=build_tree_from_list(node_list)
    print(solution.isValidBST(root))
    