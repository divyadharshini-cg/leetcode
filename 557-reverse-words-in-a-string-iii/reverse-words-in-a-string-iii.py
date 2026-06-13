class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        result=" ".join(w[::-1] for w in s)
        return result