# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head:ListNode) -> ListNode:
        current=head
        value=[]
        answer_head=ListNode()
        current2=answer_head
        while (current!=None):
            value.append(current.val)
            current=current.next
        value=sorted(value) 
        for item in value:
            new_node=ListNode(item)
            current2.next=new_node
            
            current2=current2.next
        return answer_head.next


if __name__ == "__main__":
    head = [-1,5,3,4,0]
    head_node=ListNode()
    current=head_node
    for item in head:
        new_node=ListNode(item)
        current.next=new_node
        current=current.next
    Solution=Solution()
    answer=Solution.sortList(head_node.next)
    while(answer!=None):
        print(answer.val)
        answer=answer.next    
        

