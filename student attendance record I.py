class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1

        if absent < 2 and "LLL" not in s:
            return True
        return False