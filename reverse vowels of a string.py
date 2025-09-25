class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelstring = "aeiouAEIOU"
        vowels = []
        mystr = ""
        for i in range(len(s)):
            if s[i] in vowelstring:
                vowels.append(s[i])
        k = len(vowels) - 1
        for i in range(len(s)):
            if s[i] in vowelstring:
                mystr += vowels[k]
                k-=1
            else:
                mystr+=s[i]
        return mystr