class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)

        notinArray = []
        length = len(nums)

        for i in range(length):
            if i + 1 not in num_set:
                notinArray.append(i + 1)

        return notinArray