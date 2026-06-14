class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = {}

        for num in arr:
            d[num] = d.get(num, 0) + 1

        seen = set()

        for count in d.values():
            if count in seen:
                return False
            seen.add(count)

        return True