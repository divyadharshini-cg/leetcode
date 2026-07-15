class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        odds=evens=0
        for i in range(1,n*2):
            if i%2==0:
                odds+=i
            else:
                evens+=i
        while evens:
            odds, evens = evens, odds % evens
        return odds