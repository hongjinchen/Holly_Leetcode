#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    #self代表solution这个类，把这个对象打包起来
    def removeNthFromEnd(self, head: ListNode,
                         n: int) -> ListNode:
        current_node = head
        depth = 0
        while (current_node):
            current_node = current_node.next
            depth = depth + 1

        if depth == n:
            head = head.next
            return head

        #current_node=head
        #for index in range(depth-n-1):
        #   current_node=current_node.next
        #if current_node.next.next:
        #    current_node.next=current_node.next.next
        #else:
        #    current_node.next.val=None
        #return head

        dummy = ListNode(0, head)
        current_node = dummy
        for i in range(1, depth - n + 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        return dummy.next

a=Solution()
head=ListNode(1)
first_node=ListNode(2)
seconde_node=ListNode(2)
third_node=ListNode(4)
forth_node=ListNode(5)
head.next=first_node
first_node.next=seconde_node
seconde_node.next=third_node
third_node.next=forth_node
result=a.removeNthFromEnd(head,2)
while (result):
    print(result.val)
    result = result.next
