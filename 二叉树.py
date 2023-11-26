# 二叉树

class TreeNode():
    def __init__(self,val,left=None,right=None):

        self.val=val
        self.left=left
        self.right=right



Node1=TreeNode(1)
Node2=TreeNode(2)
Node3=TreeNode(3)
Node4=TreeNode(4)
Node5=TreeNode(5)

Node1.left=Node2
Node1.right=Node3
Node3.left=Node4
Node3.right=Node5

# 根，左，右--前序遍历
current_node=Node1
# def digui(current_node):
#     if current_node!=None:
#         print(current_node.val)
#         digui(current_node.left)
#         digui(current_node.right)
# digui(current_node)
node_list=[]
pre_node=Node1
while current_node!=None:
    if current_node not in node_list:
        print(current_node.val)
    node_list.append(current_node)
    
    if current_node.left!=None:
        pre_node=current_node
        if current_node.left not in node_list:
            current_node=current_node.left

    elif current_node.right!=None:
        pre_node=current_node
        if current_node.right not in node_list:
            current_node=current_node.right
    else:
        # 当前节点为叶子节点，没有子树-回退
        current_node=pre_node