# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head

        while current:
            next = current.next # save the next node
            current.next = prev # assign the current next to point to previous
            prev = current # move the previous the current
            current = next # move the current to the next

        return prev