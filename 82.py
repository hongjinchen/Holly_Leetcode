# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # # 如何判断重复？因为已排序，所以如果当前节点的值和下一个节点的值相同，那么存在重复的情况，并且删除下一个节点
        # head=head
        # current_node=head

        # while current_node.next!=None:
        #     if current_node.val==current_node.next.val:
        #         if current_node.next.next==None:
        #             current_node.next=None
        #             break
        #         current_node.next=current_node.next.next
        #         current_node=current_node.next
        #     else:
        #         current_node=current_node.next
        # # 返回 已排序的链表，返回head
        # return head

        if head== None:
            return None

        if head.next==None:
            return head
        # 解决删除头节点的问题！
        dummy = ListNode(0, head)
        current_node=head
        prev_node=dummy
        # while current_node.next!=None:
        #     if current_node.val==current_node.next.val:
        #         if current_node.next.next==None:
        #             prev_node.next=None
        #             break
        #         while current_node.val==current_node.next.val:
        #             current_node.next=current_node.next.next
        #             if current_node.next==None:
        #                 prev_node.next=None
        #                 break
        #         prev_node.next=current_node.next
        #         current_node=current_node.next
        #     else:
        #         prev_node=current_node
        #         current_node=current_node.next
        
        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                # 删除所有重复的节点
                while current_node.next and current_node.val == current_node.next.val:
                    current_node = current_node.next
                # 将 prev_node 的 next 指向 current_node 的下一个节点，从而删除当前一系列重复的节点
                prev_node.next = current_node.next
            else:
                prev_node = current_node  # 如果没有重复，更新 prev_node
            
            current_node = current_node.next  # 移动到下一个节点
        # 返回 已排序的链表，返回head
        return dummy.next

if __name__=="__main__":
    s = Solution()
    head = [1,1,1]
    H=ListNode(head[0])
    T=H
    for index in range(1,len(head)):
        item=head[index]
        new_node = ListNode(item)
        T.next = new_node
        T = T.next
    answer=s.deleteDuplicates(H)
    while(answer!=None):
        print(answer.val)
        answer=answer.next