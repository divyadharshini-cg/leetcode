class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        count=defaultdict(lambda: defaultdict(int))
        win=set()
        for p,c in pick:
            count[p][c]+=1
            if count[p][c]>p:
                win.add(p)
        return len(win)