# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
# 请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head==None:
            return None
        if head.next==None:
            return head
        
        if left==right:
            return head
        
        if left>right:
            new_left=right
            new_right=left
            left=new_left
            right=new_right

        count=1
        dummy=ListNode(0,head)
        current_node=head
        left_node=None
        right_node=None
        value_list=[]
        while current_node:
            if count==left:
                left_node=current_node
            if count==right:
                right_node=current_node
            value_list.append(current_node.val)
            
            current_node=current_node.next
            count+=1

        while left_node!=right_node:
            left_node.val=value_list[right-1]
            left_node=left_node.next
            right-=1

        right_node.val=value_list[left-1]

        return dummy.next





if __name__=="__main__":
    solution=Solution()
    head=[3,5]
    left=1
    right=2
    
    H=ListNode(head[0])
    T=H
    for index in range(1,len(head)):
        item=head[index]
        new_node=ListNode(item)
        T.next=new_node
        T=T.next

        if index==left-1:
            left_node=new_node
        elif index==right-1:
            right_node=new_node
    
    answer=solution.reverseBetween(H,left,right)
    while(answer!=None):
        print(answer.val)
        answer=answer.next
    
    
