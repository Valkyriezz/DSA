class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        stack=[]
        ans=[]
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            if i<n:
                if stack==[]:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
            stack.append(nums[i%n])
        return ans[::-1]
        