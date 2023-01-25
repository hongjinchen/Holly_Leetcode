# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。如果节点是在末尾，需要放在head
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length=0
        newNode=ListNode()
        # 创建一个空的node，并且将它添加为head，为最后一位的数字做准备
        currentNode=head
        head=newNode
        head.next=currentNode
        finalValue=-1
        while currentNode.next.next:
            currentNode=currentNode.next
            length=length+1
        length=length+1
        finalValue=currentNode.next.val
        head.val=finalValue
        currentNode.next=head
        k=k-1

        for number in range(k):
            currentNode=head
            for index in range(length):
                currentNode=currentNode.next
            head=currentNode
        return head

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    k = 2
    head=ListNode()
    head.val=nums[0]
    currentNode=head
    for index in range(1,len(nums)):
        newNode=ListNode()
        newNode.val=nums[index]
        currentNode.next=newNode
        currentNode=currentNode.next
        
    Solution=Solution()
    answer=Solution.rotateRight(head,k)
    print("?")
    now=answer
    while(now.next!=None):
        print(now.val)
        now=now.next
    
