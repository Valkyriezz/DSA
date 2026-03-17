class Solution(object):
    def largestRectangleArea(self,nums):
        n=len(nums)
        # left=[0]*n
        # right=[0]*n
        # stack=[]
        # for i in range(n):
        #     while stack and heights[i]<=heights[stack[-1]]:
        #         stack.pop()
        #     if stack:
        #         left[i]=i-stack[-1]
        #     else:
        #         left[i]=i+1
        #     stack.append(i)
        # stack=[]
        # for i in range(n-1,-1,-1):
        #     while stack and heights[i]<=heights[stack[-1]]:
        #         stack.pop()
        #     if stack:
        #         right[i]=stack[-1]-i
        #     else:
        #         right[i]=n-i
        #     stack.append(i)
        # maxi=0
        # for i in range(n):
        #     curr=heights[i]*(left[i]+right[i]-1)
        #     maxi=max(curr,maxi)
        # return maxi
        maxi=0
        stack=[]
        i=0
        pse=-1
        while i<n:
            while stack and nums[stack[-1]]>nums[i]:
                x=stack.pop()
                nse=i
                pse=-1
                if stack:
                    pse=stack[-1]
                else:
                    pse=-1
                area=nums[x]*(nse-pse-1)
                maxi=max(area,maxi)
            stack.append(i)
            i+=1
        while stack:
            nse=n
            x=stack.pop()
            pse=-1
            if stack:
                pse=stack[-1]
            else:
                pse=-1
            area=nums[x]*(nse-pse-1)
            maxi=max(area,maxi)
        return maxi
    


