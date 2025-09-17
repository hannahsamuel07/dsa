class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.update({nums[i]: i})
            else:
                if abs(seen.get(nums[i]) - i) <= k:
                    return True
                else:
                    seen.update({nums[i]: i})

        return False
