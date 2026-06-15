class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r=[]
        c=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if  matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in r:
            matrix[i]=[0]*len(matrix[0])
        for i in c:
            for j in range(len(matrix)):
                matrix[j][i]=0