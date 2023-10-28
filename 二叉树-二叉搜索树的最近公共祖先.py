# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while True: 
            if p.val < cur.val and q.val < cur.val: 
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val: 
                cur = cur.right
            elif cur == p: 
                return p
            elif cur == q: 
                return q
            else: 
                break
        return cur

# 初始化当前节点为根节点（cur = root）：从根节点开始搜索。

# 无限循环（while True）：持续进行以下操作直至找到答案。

# 检查节点值：
# 如果p和q都在当前节点的左子树中（即p.val < cur.val and q.val < cur.val），则更新当前节点为其左孩子（cur = cur.left）。
# 如果p和q都在当前节点的右子树中（即p.val > cur.val and q.val > cur.val），则更新当前节点为其右孩子（cur = cur.right）。
# 检查是否找到答案：
# 如果当前节点等于p或q，那么它就是最低的公共祖先，因为另一个节点在它的子树中。
# 否则，如果当前节点满足了其中一个节点在其左子树而另一个在其右子树，或者一个节点就是当前节点，那么当前节点就是最低的公共祖先。
# 返回结果（return cur）：返回找到的最低公共祖先。

# 复杂度分析
# 时间复杂度：由于每次迭代中，你都是朝着p和q的方向移动，因此最多需要O(h)的时间，其中h是树的高度。

# 空间复杂度：这个算法只使用了常数额外空间，所以空间复杂度是O(1)。


if __name__ == "__main__":
    root=TreeNode(6)
    root.left=TreeNode(2)
    root.right=TreeNode(8)
    root.left.left=TreeNode(0)
    root.left.right=TreeNode(4)
    root.right.left=TreeNode(7)
    root.right.right=TreeNode(9)
    root.left.right.left=TreeNode(3)
    root.left.right.right=TreeNode(5)

    p=TreeNode(2)
    q=TreeNode(8)

    answer=Solution().lowestCommonAncestor(root,p,q)
    print(answer.val)