class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x // 10 == 0:
            return x
        digits = []
        x_mdfi = x
        isnegative = False
        if x < 0:
            isnegative = True
            x_mdfi *= -1
        while x_mdfi > 0:
            digits.append((x_mdfi % 10))
            x_mdfi //= 10

        multi = 1
        sum = 0
        for i in range(len(digits) - 1, -1, -1):
            sum += (digits[i] * multi)
            multi *= 10

        if isnegative:
            sum = sum * -1
        if sum > (pow(2, 31) - 1) or sum < (0 - (pow(2, 31))):
            return 0
        return sum
