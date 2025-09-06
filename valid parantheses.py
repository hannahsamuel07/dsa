class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        storage = []
        for i in range(len(s)):
            if s[i] == "(":
                storage.append(s[i])
            if s[i] == "{":
                storage.append(s[i])
            if s[i] == "[":
                storage.append(s[i])

            if s[i] == ")":
                if len(storage) == 0:
                    return False
                if storage[-1] != "(":
                    return False
                else:
                    storage.pop(-1)
            if s[i] == "]":
               if len(storage) == 0:
                    return False
               if storage[-1] != "[":
                    return False
               else:
                    storage.pop(-1)
            if s[i] == "}":
                if len(storage) == 0:
                    return False
                if storage[-1] != "{":
                    return False
                else:
                    storage.pop(-1)
        if len(storage) == 0:
            return True
        else:
            return False