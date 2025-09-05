class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:  # neg num immediate false
            return False
        xstring = str(x)
        mystr = ""
        for i in range(len(xstring)):  # iterate thru string
            mystr += xstring[len(xstring) - 1 - i]  # grab each character from the back to form a new string

        if xstring == mystr:  # compare strings
            return True
        return False