class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        mydict = {}
        for i in range(len(arr)):
            mydict.update({arr[i]: mydict.setdefault(arr[i], 0) + 1})
        mylist = mydict.values()
        # print(mylist)
        numList = len(mylist)
        numSet = len(set(mylist))

        return numSet == numList