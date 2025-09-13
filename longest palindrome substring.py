class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        tempstr = ""
        longestPalindrome = ""
        for i in range(len(s)):
            tempstr = ""
            for j in range(i, len(s), 1):
                tempstr += s[j]
                if tempstr == tempstr[::-1]:  # check palindrome
                    if len(tempstr) > len(longestPalindrome):  # check length
                        longestPalindrome = tempstr  # assign palindrome

        return longestPalindrome
