class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array = []
        for i in range(0,n):
            if (i+1)%3 == 0:
                if (i+1)%5 == 0:
                    array.append("FizzBuzz")
                else:
                    array.append("Fizz")
            else:
                if (i+1)%5 == 0:
                    array.append("Buzz")
                else:
                    array.append(str(i+1))
        return array