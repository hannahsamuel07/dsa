class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # checking s maps to t
        mydict = {}
        for i in range(len(s)):
            List = mydict.keys()  # get the list of existing keys
            if s[i] not in List:  # check if we have seen this key before
                mydict.update({s[i]: t[i]})  # if we haven't seen it add it to the doct
            else:
                if t[i] != mydict.get(s[i]):  # if we have seen it check if the value it corresponds to matches to
                    # the dict value
                    return False  # not matching => False
        # checking t maps to s
        mydict = {}
        for i in range(len(t)):
            List = mydict.keys()  # get the list of existing keys
            if t[i] not in List:  # check if we have seen this key before
                mydict.update({t[i]: s[i]})  # if we haven't seen it add it to the doct
            else:
                if s[i] != mydict.get(t[i]):  # if we have seen it check if the value it corresponds to matches to
                    # the dict value
                    return False  # not matching => False

        return True  # all the key values matched