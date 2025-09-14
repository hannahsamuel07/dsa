class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countZeroes = 0
        for x in nums:
            if x == 0:
                countZeroes += 1

        while 0 in nums:
            nums.remove(0)

        for i in range(countZeroes):
            nums.append(0)

