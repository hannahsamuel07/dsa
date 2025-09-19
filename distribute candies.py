class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        maxnum = len(candyType)/2
        uniqueCandies = set(candyType)
        numOfUniqueCandies = len(uniqueCandies)

        return min(numOfUniqueCandies, maxnum)