class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        shortestStr = strs[0]
        for x in strs:
            if len(x) < shortestStr:
                shortestStr = x
        i = 0
        searchStr = ""
        grbingByLetter = ""
        while i < len(shortestStr):
            grbingByLetter += shortestStr[i]
            for x in strs:
                if x.find(grbingByLetter) != 0:
                    return searchStr
            searchStr += shortestStr[i]
            i += 1

        return searchStr
