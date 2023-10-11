# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

# 你应当 保留 两个分区中每个节点的初始相对位置。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) ->ListNode:
        if head== None:
            return None

        if head.next==None:
            return head
        
        dummy=ListNode(0,head)
        current_node=head
        # 如果当前的节点大小小于x，那么就不用动，如果大于等于x，那么就要把这个节点挪到最后,然后在所有的节点都遍历一遍后,返回head
        # 如何将一个节点放在链表的最后呢?
        last_node=head
        node_num=0
        while current_node.next!=None:
            current_node=current_node.next
            node_num+=1
        last_node=current_node
        current_node=head
        per_node=dummy
        while current_node and current_node.next!=None and node_num>=0:
            if current_node.val>=x:
                last_node.next=ListNode(current_node.val)
                last_node=last_node.next
                per_node.next=current_node.next
                current_node=current_node.next
                node_num-=1
            else:
                per_node=current_node
                current_node=current_node.next
                node_num-=1
                
        return dummy.next



if __name__=="__main__":
    s=Solution()
    head = [1,4,3,0,5,2]
    x = 2
    H=ListNode(head[0])
    T=H
    for index in range(1,len(head)):
        item=head[index]
        new_node = ListNode(item)
        T.next = new_node
        T = T.next
    answer=s.partition(H,x)
    while(answer!=None):
        print(answer.val)
        answer=answer.next

    