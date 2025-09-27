class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        mylist = []
        j = 0
        while j < len(words):
            compareword = words[j]
            for i in range(len(words)):
                if compareword in words[i] and i!= j and compareword not in mylist:
                    mylist.append(compareword)
            j+=1
        return mylist