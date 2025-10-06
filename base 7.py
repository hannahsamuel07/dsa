class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num  == 0:
            return "0"
        remainders = []
        number = abs(num)
        while number > 0:
            remainders.append(number % 7)
            number //= 7

        print(remainders)
        mystr = ""
        if num < 0:
            mystr += '-'
        remainders.reverse()
        for x in remainders:
            mystr += str(x)
        return mystr