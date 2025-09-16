class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copyList = list(nums)
        for x in nums:
            copyList.remove(x)
            if x not in copyList:
                return x
            else:
                copyList.append(x)