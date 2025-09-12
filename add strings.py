class Solution(object):

    def decodeChar(self, char):
        if char == '0':
            return 0
        elif char == '1':
            return 1
        elif char == '2':
            return 2
        elif char == '3':
            return 3
        elif char == '4':
            return 4
        elif char == '5':
            return 5
        elif char == '6':
            return 6
        elif char == '7':
            return 7
        elif char == '8':
            return 8
        else:
            return 9

    def decodeInt(self, inty):
        if inty == 0:
            return '0'
        elif inty == 1:
            return '1'
        elif inty == 2:
            return '2'
        elif inty == 3:
            return '3'
        elif inty == 4:
            return '4'
        elif inty == 5:
            return '5'
        elif inty == 6:
            return '6'
        elif inty == 7:
            return '7'
        elif inty == 8:
            return '8'
        else:
            return '9'

    def convertStringArraytoNum(self, mystr):
        multiplier = 1
        sum = 0
        i = len(mystr) - 1
        while i >= 0:
            sum += (self.decodeChar(mystr[i]) * multiplier)
            multiplier *= 10
            i -= 1
        return sum

    def getdigitArray(self, num):
        digits = []
        if num == 0:
            digits.append(0)
        while num > 0:
            digits.append(num % 10)
            num //= 10
        digits.reverse()
        return digits

    def buildString(self, digits):
        mystr = ""
        for x in digits:
            mystr += (self.decodeInt(x))
        return mystr

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        output = ""

        sum1 = self.convertStringArraytoNum(num1)
        sum2 = self.convertStringArraytoNum(num2)

        total_sum = sum1 + sum2
        output = self.buildString(self.getdigitArray(total_sum))
        return output