N=7
weight=[1 ,2 ,3 ,3 ,2 ,5 ,1]
M=3

class TreeNode():
    def __init__(self,val=None,index=None,LeftNode=None,RightNode=None):
        self.val=val
        self.index=index
        self.LeftNode=LeftNode
        self.RightNode=RightNode

# 获得树的深度
depth=0
while N>2^depth:
    depth+=1
# 判断是否为叶子节点
if M>2^(depth-1) and M<2^depth:
    print("E")
else:
    # 如果不是叶子节点进入下面的比较
    node_list=[]
    # 创建树节点和对应的权重值
    def CreatTree(depth):
        currentIndex=1
        head=TreeNode(val=weight[0],index=1)
        currentNode=head
        node_list.append(currentNode)
        currentDepth=depth
        # BFS
        
        while currentDepth>0:
            for index in range(currentIndex,currentIndex+2^(depth-currentDepth)):
                newNode=TreeNode(val=weight[index],index=index+1)
                if index%2==0:
                    node_list[int(index/2)].LeftNode=newNode
                elif index%2==1:
                    node_list[int(index/2)].RightNode=newNode
                node_list.append(newNode)
            
            currentIndex=index+2^(depth-currentDepth)
            currentDepth-=1
        return head
    
    head=CreatTree(depth)
    
    # 寻找对应的M的node
    currentNode=head
    def findNode(currentNode,M):
        if currentNode.index==M:
            return currentNode
        
        else:
            findNode(currentNode.RightNode,M)
            findNode(currentNode.RightNode,M)
    
    MNode=findNode(currentNode,M)
    
    # 获取左子树和右子树的权重
    