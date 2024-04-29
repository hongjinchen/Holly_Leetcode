# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numebr1=self.getNumber(l1,0,0)
        number2=self.getNumber(l2,0,0)
        answer=numebr1+number2
        reversed_x = list(str(answer)[::-1])
        answer_list=list_to_linked_list(reversed_x)
        return answer_list
    
    def getNumber(self,current_node,index,total_number):
        current_value=int(str(current_node.val)+index*"0")
        total_number=total_number+current_value  
        if current_node.next==None:
            return total_number
      
        return(self.getNumber(current_node.next,index+1,total_number))
        
    def list_to_linked_list(items):
        # 创建一个虚拟头节点，简化边界条件处理
        dummy = ListNode(0)
        current = dummy
        
        # 遍历列表中的每个元素，为每个元素创建一个链表节点，并将其添加到链表的末尾
        for item in items:
            current.next = ListNode(int(item))
            current = current.next
        
        return dummy.next        

def list_to_linked_list(items):
    # 创建一个虚拟头节点，简化边界条件处理
    dummy = ListNode(0)
    current = dummy
    
    # 遍历列表中的每个元素，为每个元素创建一个链表节点，并将其添加到链表的末尾
    for item in items:
        current.next = ListNode(item)
        current = current.next
    
    # 返回头节点的下一个节点，即真正的链表的开始
    return dummy.next

if __name__=="__main__":
    
    l1 = [2,4,3]
    l2 = [5,6,4]
    
    linked_list1 = list_to_linked_list(l1)
    linked_list2 = list_to_linked_list(l2)
    
    sol=Solution()
    sol.addTwoNumbers(linked_list1,linked_list2)