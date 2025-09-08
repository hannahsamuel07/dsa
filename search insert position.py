class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    if i+1 < len(nums):
                        if target < nums[i+1]:
                            return i+1
                        else:
                            continue
                    else:
                        return i+1
                else:
                    return i