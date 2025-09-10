class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = 0
        sum_a = 0
        sum_b = 0
        i = len(a) - 1
        n = 0
        while i >= 0:
            if a[i] == '1':
                sum_a += pow(2, n)

            n += 1
            i -= 1
        i = len(b) - 1
        n = 0
        while i >= 0:
            if b[i] == '1':
                sum_b += pow(2, n)

            n += 1
            i -= 1

        sum_in_decimal = sum_a + sum_b
        if sum_in_decimal == 0:
            return '0'
        remainders = []
        while sum_in_decimal > 0:
            quot = sum_in_decimal // 2
            remain = sum_in_decimal % 2
            remainders.append(remain)
            sum_in_decimal = sum_in_decimal // 2

        remainders.reverse()
        mystr = ""
        for x in remainders:
            s = str(x)
            mystr += s

        return mystr

