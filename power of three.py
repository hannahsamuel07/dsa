class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        if n == 1:
            return True
        if n == 0:
            return False
        while n > 0:
            if n == 3: return True
            if n%3 != 0:
                return False
            n//=3
        return True