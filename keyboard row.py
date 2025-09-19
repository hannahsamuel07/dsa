class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        firstrow = "qwertyuiopQEWRTYUIOP"
        secondrow = "asdfghjklASDFGHJKL"
        thirdrow = "zxcvbnmZXCVBNM"
        rowsusing = []
        rowinfo = []
        for x in words:
            for i in range(len(x)):
                if x[i] in firstrow:
                    rowsusing.append('f')
                elif x[i] in secondrow:
                    rowsusing.append('s')
                else:
                    rowsusing.append('t')
            rowinfo.append(rowsusing)
            rowsusing = []
        finalanswer = []
        print(rowinfo)
        for i in range(len(rowinfo)):
            if 'f' in rowinfo[i]:
                if 's' not in rowinfo[i] and 't' not in rowinfo[i]:
                    finalanswer.append(words[i])
                    continue
            if 's' in rowinfo[i]:
                if 'f' not in rowinfo[i] and 't' not in rowinfo[i]:
                    finalanswer.append(words[i])
                    continue
            if 't' in rowinfo[i]:
                if 's' not in rowinfo[i] and 'f' not in rowinfo[i]:
                    finalanswer.append(words[i])
                    continue
        return finalanswer


