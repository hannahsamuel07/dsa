class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        mystr = ""
        for i in range(len(s)):
            if s[i] != ' ':
                mystr += s[i]
            else:
                if mystr != "":
                    words.append(mystr)
                mystr = ""
        if mystr != "":
            words.append(mystr)
        words.reverse()
        reversedString = ""
        for i in range(len(words)):
            reversedString += words[i]
            if i != len(words) - 1:
                reversedString += ' '

        return reversedString