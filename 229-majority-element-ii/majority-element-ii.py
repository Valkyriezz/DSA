class Solution(object):
    def majorityElement(self, nums):
        # curr=nums[0]
        # count=1
        # for i in range(1,len(nums)):
        #     if nums[i]==curr:
        #         count+=1
        #     else:
        #         count-=1
        #         if count==0:
        #             curr=nums[i]
        #             count=1
        # return [curr]
        c1=0
        c2=0
        cand1=float("-inf")  
        cand2=float("-inf") 
        for i in nums:
            if c1==0 and i!=cand2:
                cand1=i
                c1=1
            elif c2==0 and i!=cand1:
                cand2=i
                c2=1
            elif i==cand1:
                c1+=1
            elif i==cand2:
                c2+=1
            else:
                c1-=1
                c2-=1
        res=[]
        n=len(nums)
        for i in [cand1,cand2]:
            if nums.count(i)>n//3:
                res.append(i)
        return res

