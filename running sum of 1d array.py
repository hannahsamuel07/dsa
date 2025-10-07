class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        currSum = 0
        sum = []
        for i in range(len(nums)):
            currSum += nums[i]
            sum.append(currSum)

        return sum
