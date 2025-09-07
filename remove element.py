class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        temp = []
        for i in range(len(nums)):
            if nums[i] != val:
                temp.append(nums[i])

        for i in range(len(temp)):
            nums[i] = temp[i]
        k = len(temp)
        return k