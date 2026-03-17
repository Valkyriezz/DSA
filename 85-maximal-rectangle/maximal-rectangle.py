class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        rows=len(matrix)
        cols=len(matrix[0])
        heights=[0]*cols
        maxi=0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]=='1':
                    heights[c]+=1
                else:
                    heights[c]=0
            n=len(heights)
            left=[0]*n
            right=[0]*n
            stack=[]
            for i in range(n):
                while stack and heights[i]<=heights[stack[-1]]:
                    stack.pop()
                if stack:
                    left[i]=i-stack[-1]
                else:
                    left[i]=i+1
                stack.append(i)
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and heights[i]<=heights[stack[-1]]:
                    stack.pop()
                if stack:
                    right[i]=stack[-1]-i
                else:
                    right[i]=n-i
                stack.append(i)
            for i in range(n):
                maxi=max(maxi,heights[i]*(left[i]+right[i]-1))
        return maxi