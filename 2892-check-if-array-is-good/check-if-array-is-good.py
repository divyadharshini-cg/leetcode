class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        c=Counter(nums)
        if c[n-1]!=2: return False
        for num in range(1,n-1):
            if c[num]!=1:
                return False
        return True
