class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=max(nums)
        c=0
        for i in nums:
            if i*2<=s:
                c+=1
        if c==len(nums)-1:
            return nums.index(s)
        return -1