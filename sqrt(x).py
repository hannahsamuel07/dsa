class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        lowval = 0
        highval = x
        search = 0
        while lowval <= highval:
            middle = (lowval + highval) // 2
            if middle * middle == x:
                return middle
            elif middle * middle < x:
                search = middle
                lowval = middle + 1

            else:
                highval = middle - 1
        return search
