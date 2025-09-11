# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def deleteSpecificNode(self, head, nodeToDelete):  # helper function for removing the linked list
        if head == nodeToDelete:  # check if head itself is what we wanr ro remove
            return head.next
        currentNode = head  # pointer to the front of the list
        while currentNode.next != None and currentNode.next != nodeToDelete:  # iterate though searching if you find the node we need to delete
            currentNode = currentNode.next  # if its not just keep moving
        currentNode.next = nodeToDelete.next  # if it is move to point to the next node in the list (the node after the node to be deleted)

        return head  # return back to the main function

    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        referenceToHead = head  # pointer to head to keep things clean
        currentNode = head  # pointer we use to iterate
        storage = []  # storage container to store unqiue values of the nodes in the linked lit
        while currentNode:  # iterate through the linked lit
            if currentNode.val not in storage:  # check if the node's value is uniqe
                storage.append(currentNode.val)  # add the unique value to the array
                currentNode = currentNode.next  # move the list along
            else:  # we found a duplicate (it was already detected in the array)
                nodeToDelete = currentNode  # capture the node we want to delete
                self.deleteSpecificNode(referenceToHead, nodeToDelete)  # call the helper to safely remove it
                currentNode = currentNode.next  # after its removed, move to the next node because the current node no longer exists
        return head  # return the unique linked list