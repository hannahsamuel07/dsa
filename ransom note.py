class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = {}
        for i in range(len(ransomNote)):
            counter.update({ransomNote[i]: magazine.count(ransomNote[i])})

        myList = counter.keys()
        for i in range(len(ransomNote)):
            if counter.get(ransomNote[i]) == 0:
                return False
            else:
                counter.update({ransomNote[i]: counter.setdefault(ransomNote[i]) - 1})

        return True