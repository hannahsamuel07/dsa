class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        storage = []
        for i in range(len(s)):
            if s[i] not in storage:
                if s.count(s[i]) == 1:
                    return i
                else:
                    storage.append(s[i])
            else:
                pass
        return -1