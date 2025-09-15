class Solution(object):
    def createLists(self, num):
        if num == '2':
            return ['a', 'b', 'c']
        elif num == '3':
            return ['d', 'e', 'f']
        elif num == '4':
            return ['g', 'h', 'i']
        elif num == '5':
            return ['j', 'k', 'l']
        elif num == '6':
            return ['m', 'n', 'o']
        elif num == '7':
            return ['p', 'q', 'r', 's']
        elif num == '8':
            return ['t', 'u', 'v']
        else:
            return ['w', 'x', 'y', 'z']

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        listofStrings = []
        possibleLists = []

        result = [""]  # create an empty list with just an empty string
        for char in digits:  # iterate though the given digits
            List = self.createLists(char)  # for each digits get the associate list of letters
            newList = []  # create a new list to save our possible combos
            for p in result:  # go through the list
                for c in List:  # go through each char in the letter lists
                    newList.append(p + c)  # append each letter to the list
            result = newList  # make the resulting list equal to the new list just built
        return result
