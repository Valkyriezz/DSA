class Solution(object):
    def asteroidCollision(self, nums):
        stack=[]
        i=0
        n=len(nums)
        while i<n:
            if nums[i]>0:
                stack.append(nums[i])
                i+=1
            else:
                while stack and stack[-1]>0:
                    if stack[-1]<-nums[i]:
                        stack.pop()
                        continue
                    elif stack[-1]==-nums[i]:
                        stack.pop()
                    break
                else:
                    stack.append(nums[i])
                i+=1
        return stack
                
        
        