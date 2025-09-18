class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = {}
        for i in range(len(t)):
            counter.update({t[i]: s.count(t[i])})

        for i in range(len(t)):
            if counter.get(t[i]) == 0:
                return t[i]
            else:
                counter.update({t[i]: counter.setdefault(t[i]) - 1})



