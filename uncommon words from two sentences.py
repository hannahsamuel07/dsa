class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        output = []
        first = []
        second = []
        tempstr = ""
        for i in range(len(s1)):
            if s1[i]!= ' ':
                tempstr += s1[i]
            else:
                if tempstr != "":
                    first.append(tempstr)
                    tempstr = ""
        if tempstr!= "":
            first.append(tempstr)
        tempstr = ""
        for i in range(len(s2)):
            if s2[i]!= ' ':
                tempstr += s2[i]
            else:
                if tempstr != "":
                    second.append(tempstr)
                    tempstr = ""
        if tempstr!= "":
            second.append(tempstr)
        for word in first:
            if word not in second and first.count(word) == 1:
                output.append(word)
        for word in second:
            if word not in first and second.count(word) == 1:
                output.append(word)
        return output