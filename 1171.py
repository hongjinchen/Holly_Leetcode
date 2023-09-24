# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:



if __name__ == "__main__":
    solution=Solution()
    head = [1,2,-3,3,1]
    print(solution.removeZeroSumSublists(head))   