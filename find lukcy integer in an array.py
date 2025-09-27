class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = 0
        j = 0
        mydict = {}
        while j < len(arr):

            for i in range(len(arr)):
                if arr[j] == arr[i]:
                    counter+=1
            if counter == arr[j]:
                mydict.update({arr[j]: counter})
            j+=1
            counter = 0
        mylist = mydict.keys()
        if len(mylist) == 0:
            return -1
        maxval = mylist[0]
        for i in range(len(mylist)):
            if mylist[i] > maxval:
                maxval = mylist[i]
        return maxval