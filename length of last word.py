class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        store = []
        temp = ""
        for char in range(len(s)):
            if s[char] != ' ':
                temp += s[char]
                if char == len(s) - 1:
                    store.append(temp)
                    temp = ""
            else:
                store.append(temp)
                temp = ""
        i = len(store) - 1
        while i >= 0:
            if store[i] != "":
                return len(store[i])
            else:
                i-=1