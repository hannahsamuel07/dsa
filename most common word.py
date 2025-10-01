class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        mylist = []
        tempstr = ""
        for i in range(len(paragraph)):
            mystr = paragraph[i]
            if mystr.isalpha():
                tempstr += mystr
            else:
                if tempstr != "":
                    mylist.append(tempstr.lower())
                tempstr = ""
        if tempstr.isalnum():
            mylist.append(tempstr.lower())
        mydict = {}
        for word in mylist:
            mydict[word] = mydict.get(word, 0) + 1

        mostCommonword = ""
        max = 0
        for x, y in mydict.items():
            if x not in banned:
                if y > max:
                    max = y
                    mostCommonword = x
        return mostCommonword