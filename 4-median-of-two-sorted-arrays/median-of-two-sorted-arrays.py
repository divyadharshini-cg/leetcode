class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        c=(nums1+nums2)
        c.sort()
        n=len(c)
        if n%2!=0:
            return c[n//2]
        else:
            return (c[n//2-1]+c[n//2])/2.0
 
