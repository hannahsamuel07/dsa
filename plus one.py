class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
        else:
            found_non_zero = False
            # find the next closest digit that is not 9
            i = len(digits) - 1
            while i >= 0:
                if digits[i] != 9:
                    digits[i] += 1
                    found_non_zero = True
                    break
                else:
                    digits[i] = 0
                    i -= 1

            if found_non_zero == False:  # case where we never found a non nine and the array ended
                digits[0] = 1  # assign first digit to 1 because a leading 9 always follows a 1 in addition
                digits.append(0)  # append a zero to create the new total after adding 1
                # ex: 999 -> 000 -> 100 -> 1000
                # 999 + 1 = 1000s
        return digits
