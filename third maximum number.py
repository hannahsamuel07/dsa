class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            firstMax = nums[0]
            for x in nums:
                if x > firstMax:
                    firstMax = x
            return firstMax
        firstMax = nums[0]
        for x in nums:
            if x > firstMax:
                firstMax = x
        while firstMax in nums:
            nums.remove(firstMax)
        if len(nums) == 0:
            return firstMax
        secondMax = nums[0]
        for x in nums:
            if x > secondMax:
                secondMax = x
        while secondMax in nums:
            nums.remove(secondMax)
        if len(nums) == 0:
            return firstMax
        thirdMax = nums[0]
        for x in nums:
            if x > thirdMax:
                thirdMax = x
        return thirdMax