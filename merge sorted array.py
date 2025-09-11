class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        myarray = [] # storage container
        for i in range(0,m): # grab the the first m elements from nums1
            myarray.append(nums1[i])
        for i in range(0,n): # grab the first n elements from nums2
            myarray.append(nums2[i])
        myarray.sort() # sort the array
        for i in range(len(nums1)): # assign the sorted values to the first m+n spots in nums 1
            nums1[i] = myarray[i]

        #no need to return anything