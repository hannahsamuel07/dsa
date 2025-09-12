# Definition for singly-linked list.
"""class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        refl1 = l1
        refl2 = l2

        multipler1 = 1
        sum1 = 0
        while refl1:
            sum1 += (multipler1 * refl1.val)
            multipler1 *= 10
            refl1 = refl1.next

        multipler2 = 1
        sum2 = 0
        while refl2:
            sum2 += (multipler2 * refl2.val)
            multipler2 *= 10
            refl2 = refl2.next

        total_sum = sum1 + sum2
        headpointer = ListNode()  # create an empty node
        curr = headpointer
        if total_sum == 0:
            return ListNode(0)

        while total_sum > 0:
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
            total_sum //= 10

        return headpointer.next