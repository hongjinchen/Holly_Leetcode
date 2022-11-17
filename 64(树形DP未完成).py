from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def closeLampInTree(self, root: TreeNode) -> int:
        
        step=0
        q = Queue()
        q.put(root)
        while not q.empty():
            Current=q.get()
            if self.switchOne(Current):
                step=step+1
            elif self.switchTwo(Current):
                step=step+1
            elif self.switchThree(Current):
                step=step+1
            if Current.left:
                q.put(Current.left)
            if Current.right:
                q.put(Current.right)
        return step
    def switchOne(self,node:TreeNode):
        # 开关 1：切换当前节点的灯的状态；只有root灯状态为1
        if node.val==1:
            if node.left:
                if node.left.val==0:
                    if node.right:
                        if node.right.val==0:
                            node.val=self.changeValue(node.val)
                            return True
        return False
    def switchTwo(self,node:TreeNode):
        # 开关 2：切换 以当前节点为根 的子树中，所有节点上的灯的状态;root为0，两个节点为1
        if node.val==0:
            if node.left:
                if node.right:
                    if node.left.val==1 and node.right.val==1:
                        node.left.val=self.changeValue(node.left.val)
                        node.right.val=self.changeValue(node.right.val)
                        return True
        return False
    def switchThree(self,node:TreeNode):
        # 开关 3：切换 当前节点及其左右子节点（若存在的话） 上的灯的状态；root和两个节点的值都为1
        if node.val==1:
            if node.left and node.right:
                if node.left.val==1 and node.right.val==1:
                    node.right.val=self.changeValue(node.right.val)
                    node.left.val=self.changeValue(node.left.val)
                    
                    return True
            if node.right and not node.left:
                if node.right.val==1:
                    node.right.val=self.changeValue(node.right.val)
                    
                    return True
            if node.left and not node.right:
                if node.left.val==1:
                    node.left.val=self.changeValue(node.left.val)
                    
                    return True
        return False

    def changeValue(self,value):
        if value==1:
            return 0
        else:
            return 1

if __name__ == "__main__":
    list= [1,1,1,1,None,None,1]
    index=0
    Root=None
    CurrentNode=None
    for item in list:
        if index==0:
            Root=TreeNode(item)
            CurrentNode=Root
            index=index+1
        elif index%2==0:
            newNode=TreeNode(item)
            CurrentNode.right=newNode
        elif index%2==1:
            newNode=TreeNode(item)
            CurrentNode.left=newNode
    solution=Solution()
    print(solution.closeLampInTree(Root))
