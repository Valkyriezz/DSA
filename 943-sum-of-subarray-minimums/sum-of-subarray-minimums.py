class Solution(object):
    def sumSubarrayMins(self, nums):
        mod=10**9+7
        n=len(nums)
        total=0
        # for i in range(n):
        #     mini=float("inf")
        #     for j in range(i,n):
        #         mini=min(mini,nums[j])
        #         # print(mini)
        #         total=(total+mini)%mod
        # return total

        # now this gives tle ofcourse we need to know how particular element in the subaaray is contributing how many times 
        # in order to do that check the window of that particular element to the right and left in order to know the next smaller and greater element (bsaically elements right and left side boundary)
        # for each element know the pse(previous smaller element )
        # and next greater element nge 
        # do simple maths nums[i]*i-pse[i]*i-nums[i]=subbarays it is contributing to
        stack=[]
        psearr=[-1]*n
        nsearr=[n]*n
        def pse(psearr):
            for i in range(n):
                while stack and nums[stack[-1]]>nums[i]:
                    stack.pop()  
                if stack==[]:
                    psearr[i]=-1
                else:
                    psearr[i]=stack[-1]
                stack.append(i) 
        # stack=[]
        def nge(ngearr):
            stack[:]=[]
            for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]]>=nums[i]:
                    stack.pop()  
                if stack==[]:
                    nsearr[i]=n
                else:
                    nsearr[i]=stack[-1]
                stack.append(i) 
        pse(psearr)
        nge(nsearr)
        for i in range(n):
            left=i-psearr[i]
            right=nsearr[i]-i
            total=(total+nums[i]*left*right)%mod
        return total