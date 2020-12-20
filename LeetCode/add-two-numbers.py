# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def to_num(self, l1: ListNode):
        s = ''
        while l1:
            s = s+str(l1.val)
            l1 = l1.next
        return(int(s[::-1]))
    
    def to_listNode(self, n: int):
        s = str(n)
        s_list = ListNode(int(s[0]))
        for ch in s[1:]:
            s_temp = ListNode(int(ch))
            s_temp.next = s_list
            s_list = s_temp
            
        return(s_list)
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = self.to_num(l1) + self.to_num(l2)
        
        return(self.to_listNode(result))
            