class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        stringOne = ""
        stringTwo = ""
        for char in word1:
            stringOne += char
        for char in word2:
            stringTwo += char
        return stringOne == stringTwo