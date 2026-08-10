class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cycle=2*(n-1)
        p=k%cycle
        if p<=n-1:
            return p
        return cycle-p