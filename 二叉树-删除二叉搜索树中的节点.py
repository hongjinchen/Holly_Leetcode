# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

# 一般来说，删除节点可分为两个步骤：

# 首先找到需要删除的节点；
# 如果找到了，删除它。

# 输入：root = [5,3,6,2,4,null,7], key = 3
# 输出：[5,4,6,2,null,null,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
            return root
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
            return root
        else:
            if not root.right or not root.left:
                return root.right if root.right else root.left#两子树均不存在则返回None
            else:
                new=root.right
                while new.left:
                    new=new.left
                root.val=new.val#修改节点的值为新节点的值
                root.right=self.deleteNode(root.right,new.val)
                return root

        # head=TreeNode(0)
        # head.right=root
        # def helper(root,key):
        #     if root is None:
        #         return root
            
        #     if root.val==key:

        #         # 没有子节点或者有一个为空
        #         if not root.right or not root.left:
        #             return root.right if root.right else root.left#两子树均不存在则返回None
                
        #         # 两个子节点都不为空
        #         else:
        #             new=root.right
        #             while new.left:
        #                 new=new.left
        #             root.val=new.val#修改节点的值为新节点的值
        #             root.right=self.deleteNode(root.right,new.val)
        #             return root
                    
        #     elif root.val>key:
        #         root.left=self.deleteNode(root.left,key)
        #         return root
            
        #     elif root.val<key:
        #         root.right=self.deleteNode(root.right,key)
        #         return root

        # helper(root,key)
        # return head.right


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
    root_list = [5,3,6,2,4,None,7]
    key = 3
    root = build_tree_from_list(root_list)
    answer=solution.deleteNode(root,key)
    print(preorder_traversal(answer))
    