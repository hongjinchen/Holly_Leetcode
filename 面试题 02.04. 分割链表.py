# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

# 你不需要 保留 每个分区中各节点的初始相对位置。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        pre_node=head        
        null_node=ListNode()
        null_node.next=head

        while head.next!=None:
            head=head.next
            
            if head.val<x:
                pre_node.next=head
            


if __name__=="__main__":
    solution=Solution()
    list = [1,4,3,2,5,2]
    x = 3
    
    head=ListNode(1)
    pre_node=head
    for index in range(1,len(list)):
        new_node=ListNode(list[index])
        pre_node.next=new_node
        
    solution.partition(head,x)