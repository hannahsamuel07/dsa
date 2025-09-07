# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # case of both empty
        if list1 == None and list2 == None:
            return list1
        # case of list1 empty
        if list1 == None:
            return list2
        # case of list 2 empty
        if list2 == None:
            return list1

        # both lists have stuff
        mergedLinkedList = ListNode()  # create an empty linked list
        current = mergedLinkedList  # need a pointer to the new merged linked list we we can move around while always have a reference to the start of the new list
        while list1 != None and list2 != None:
            if list1.val <= list2.val:  # compare lists
                current.next = list1  # make merges point to lower value
                list1 = list1.next  # move the list1 to the next value
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1 != None:
            current.next = list1
        if list2 != None:
            current.next = list2
        return mergedLinkedList.next