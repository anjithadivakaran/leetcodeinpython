# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # intitalize variables to hold carry, sum and also create a linkedlist.
        carry = 0
        newList = ListNode(0)
        temp = newList
        totalsum = 0

        # loop over the linked list until the end of list and carry

        while l1 or l2 or carry:
        	if l1:
        		totalsum += l1.val
        		l1 = l1.next   # moving to next list
        	if l2:
        		totalsum += l2.val
        		l2 = l2.next
        	totalsum += carry
        	carry = totalsum // 10   # checks for carry over
        	temp.next = ListNode( totalsum % 10)     # appends the number to the linked list 
        	totalsum = 0   # resetting the number = 0 else the sum keep on increasing 
        	temp = temp.next 

        return newList.next 