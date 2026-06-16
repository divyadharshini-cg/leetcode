class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for i in s:
            if i.isalpha():
                res.append(i)
            elif i=="*":
                if res: 
                 res.pop()
            elif i=="#":
                res+=res
            elif i=="%":
                res.reverse()
        return "".join(res)
            