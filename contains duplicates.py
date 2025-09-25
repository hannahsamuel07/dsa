class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        amtList = len(nums)
        myset = set(nums)
        amtSet = len(myset)
        if amtList != amtSet:
            return True
        return False