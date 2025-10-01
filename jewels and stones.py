class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
                counter += 1
        return counter