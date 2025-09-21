class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = ""
        number = num
        while number > 0:
            binary+=str(number%2)
            number//=2
        binary = binary[::-1]

        intTostring = str(binary)
        newstring = ""
        for i in range(len(intTostring)):
            if intTostring[i] == '0':
                newstring+='1'
            else:
                newstring+='0'
        exponent = 0
        decimal = 0
        for i in range(len(newstring) - 1, -1, -1):
            if newstring[i] == '0':
                exponent +=1
            else:
                decimal += pow(2,exponent)
                exponent +=1
        return decimal