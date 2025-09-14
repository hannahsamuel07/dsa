class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringToInt = 0
        isNegative = False
        reachedNonZero = False
        digits = []
        reachedNonNum = False
        reachedNum = False
        justReadSign = False
        for i in range(len(s)):
            if reachedNonNum == True:
                break
            if s[i].isspace() == True:
                if reachedNum:
                    break
                if justReadSign:
                    break
            elif s[i] == '-':
                if reachedNum:
                    break
                if justReadSign:
                    break
                isNegative = True
                justReadSign = True
            elif s[i] == '+':
                if reachedNum:
                    break
                if justReadSign:
                    break
                justReadSign = True
            elif s[i] == '0':
                reachedNum = True
                if reachedNonZero:
                    reachedNum = True
                    digits.append(int(s[i]))
            else:
                if s[i].isdigit() == False :
                    reachedNonNum = True
                else:
                    reachedNum = True
                    reachedNonZero = True
                    digits.append(int(s[i]))

        if len(digits) == 0:
            return 0
        multi = 1
        for i in range(len(digits) - 1, -1, -1):
            stringToInt += (multi*digits[i])
            multi *= 10
        if isNegative:
            stringToInt =  -1 * stringToInt
        if stringToInt < (pow(2*-1, 31)):
            stringToInt = pow(2*-1, 31)
        if stringToInt > (pow(2, 31) - 1):
            stringToInt = (pow(2, 31) - 1)
        return stringToInt
