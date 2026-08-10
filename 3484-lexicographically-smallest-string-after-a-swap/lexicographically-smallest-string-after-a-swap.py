class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        for i in range(len(s)-1):
            if (int(s[i])%2)==(int(s[i+1])%2):
                if s[i]>s[i+1]:
                    s[i],s[i+1]=s[i+1],s[i]
                    break
                i+=1
        return "".join(s)