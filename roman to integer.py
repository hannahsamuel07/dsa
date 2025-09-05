class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        skip = False
        for x in range(len(s)):
            if skip == True:
                skip = False
                continue
            if s[x] == "M":
                sum += 1000
            elif s[x] == "D":
                sum += 500
            elif s[x] == "C":
                if x + 1  < len (s) and s[x+1] == "D":
                    sum += (500-100)
                    skip = True
                elif x + 1 < len (s) and s[x+1] == "M":
                    sum += (1000 - 100)
                    skip = True
                else:
                    sum +=100
            elif s[x]  == "L":
                sum +=50
            elif s[x] == "X":
                if x + 1 < len (s) and s[x+1] == "L":
                    sum += (50-10)
                    skip = True
                elif x + 1 < len (s) and s[x+1] == "C":
                    sum += (100 - 10)
                    skip = True
                else:
                    sum +=10
            elif s[x] == "V":
                sum +=5
            elif s[x] == "I":
                if x + 1 < len(s) and s[x+1] == "V":
                    sum += (4)
                    skip = True
                elif x + 1 < len (s) and s[x+1] == "X":
                    sum += (9)
                    skip = True
                else:
                    sum +=1
            else:
                sum +=0
        return sum