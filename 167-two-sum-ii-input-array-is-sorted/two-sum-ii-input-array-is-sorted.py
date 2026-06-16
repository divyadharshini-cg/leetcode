class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        s=0
        e=n-1
        for i in range(n):
            if numbers[s]+numbers[e]==target:
                return [s+1,e+1]
            if numbers[s]+numbers[e]>=target:
                e-=1
            else:
                s+=1
        