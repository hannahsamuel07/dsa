class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        storage = ""
        substr = []
        j = 0
        i = 0
        while j <= len(s) - 1:

            i = j
            while i <= len(s) - 1:
                if s[i] not in storage:
                    storage += s[i]
                else:
                    substr.append(storage)
                    storage = ""
                    break
                i += 1
            j += 1
        substr.append(storage)
        maxstr = ""
        for strs in substr:
            if len(strs) > len(maxstr):
                maxstr = strs
        return len(maxstr)
