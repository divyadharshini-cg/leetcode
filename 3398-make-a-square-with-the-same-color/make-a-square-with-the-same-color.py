class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        for row in range(2):
            for col in range(2):
                b=0
                for r in range(row,row+2):
                    for c in range(col,col+2):
                        if grid[r][c]=='B':
                            b+=1
                if b>=3 or b<=1:
                    return True
        return False