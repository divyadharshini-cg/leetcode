class Solution(object):
    def heightChecker(self, nums):
        """
        :type heights: List[int]
        :rtype: int
        """
        c=0
        ans=sorted(nums)
        for i in range(len(nums)):
            if nums[i]!=ans[i]:
                c+=1
        return c