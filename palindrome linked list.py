# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        myarray = []
        curr = head
        while curr:
            myarray.append(curr.val)
            curr = curr.next
        reversedArray = myarray[::-1]

        for i in range(len(myarray)):
            if myarray[i] != reversedArray[i]:
                return False

        return True