class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        hashmap={}
        res=[]
        n=len(nums)
        for i in range(n-1,-1,-1):
            if stack==[]:
                res.append(-1)
            elif nums[i]<stack[-1]:
                res.append(stack[-1])
            else:
                while stack and stack[-1]<=nums[i]:
                    stack.pop()
                if stack:
                    res.append(stack[-1])
                else:
                    res.append(-1)
            stack.append(nums[i])
        res=res[::-1]
        for i in range(n):
            if res[i]==-1:
                j=(i+1)%n
                while j!=i:
                    if nums[j]>nums[i]:
                        res[i]=nums[j]
                        break
                    j=(j+1)%n
        return res