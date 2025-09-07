class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        storageArray = []
        for x in nums:
            if x not in storageArray:
                storageArray.append(x)

        k = len(storageArray)
        for i in range(len(storageArray)):
            nums[i] = storageArray[i]
        return k