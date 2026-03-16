class Solution(object):
    def subArrayRanges(self, nums):
        # mod=10**9+7
        n=len(nums)
        # total=0
        # for i in range(n):
        #     mini=float("inf")
        #     maxi=float("-inf")
        #     for j in range(i,n):
        #         mini=min(mini,nums[j])
        #         maxi=max(maxi,nums[j])
        #         diff=maxi-mini
        #         total=(total+diff)
        # return total
        
        # can we use the previous question function and then larget-smallest
        # find the subarray minimum and subarray maximum
        # then largest-smallest will we our answer 

        def f1(nums):
            total=0
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
            def nse(ngearr):
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
            nse(nsearr)
            for i in range(n):
                left=i-psearr[i]
                right=nsearr[i]-i
                total=(total+nums[i]*left*right)
            return total
        smallest=f1(nums)
        
        def f2(nums):
            total=0
            stack=[]
            pgearr=[-1]*n
            ngearr=[n]*n
            def pge(psearr):
                for i in range(n):
                    while stack and nums[stack[-1]]<nums[i]:
                        stack.pop()  
                    if stack==[]:
                        pgearr[i]=-1
                    else:
                        pgearr[i]=stack[-1]
                    stack.append(i) 
            # stack=[]
            def nge(ngearr):
                stack[:]=[]
                for i in range(n-1,-1,-1):
                    while stack and nums[stack[-1]]<=nums[i]:
                        stack.pop()  
                    if stack==[]:
                        ngearr[i]=n
                    else:
                        ngearr[i]=stack[-1]
                    stack.append(i) 
            pge(pgearr)
            nge(ngearr)
            for i in range(n):
                left=i-pgearr[i]
                right=ngearr[i]-i
                total=(total+nums[i]*left*right)
            return total
        largest=f2(nums)
        return largest-smallest