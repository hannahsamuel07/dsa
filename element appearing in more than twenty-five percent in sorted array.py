class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mydict = {}
        for x in arr:
            mydict.update({x:mydict.setdefault(x,0)+1})
        keys = mydict.keys()
        print(keys)
        for x in keys:
            if mydict.get(x) / float(len(arr)) > 0.25:
                return x