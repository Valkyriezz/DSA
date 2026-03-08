class Solution(object):
    def rotate(self, matrix):
        #transpose
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # reversed
        for i in range(n):
            print(matrix[i])
            matrix[i]=list(reversed(matrix[i]))    
        return matrix
        