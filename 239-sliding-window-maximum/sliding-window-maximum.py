# push the element and rearrange
# bada hogya to nikalo
# perfect hai to ans lelo
# increament r
class Solution(object):
#     ----------------------------------
# <-                     3 -1                 <-
#     ----------------------------------
    def maxSlidingWindow(self, nums, k):
        queue=deque()
        l=0
        r=0
        n=len(nums)
        res=[]
        # print(queue.top())
        while r<n:
            while queue and queue[-1]<nums[r]:
                queue.pop()
            queue.append(nums[r])
            
            if r-l+1>k:
                #imp
                if nums[l]==queue[0]:
                    queue.popleft()
                l+=1
            if r-l+1==k:
                res.append(queue[0])
                
            # if r-l+1<k:
            #     while queue and queue[-1]<nums[r]:
            #         queue.pop()
            #     queue.append(num[r])
            # elif r-l+1==k:
            #     res.append(queue[0])
            # else:
            #     if nums[l]==queue[0]:
            #         queue.popleft()
            #     l+=1
            r+=1
        return res
                