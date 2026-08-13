# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # now that we have the middle of the list
        # we reverse the res 
        current = slow.next 
        slow.next = None # we break the list
        prev = None
        while current:
            temp = current.next
            current.next = prev # gets set to none initially
            prev = current # increment the previous
            current = temp
        # this should result the second list being reversed
        l2 = prev # this is the head of the current list
        l1 = head # reset
        l2
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next 
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2


        