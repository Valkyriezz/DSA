class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n=len(nums)
        memo={}
        def f(i,prev):
            if i<0:
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]
            nottake=f(i-1,False)
            take=0
            if not prev:
                take=nums[i]+f(i-1,True)
            else:
                #it was take check clr
                if colors[i]!=colors[i+1]:
                    take=nums[i]+f(i-1,True)
            memo[(i,prev)]=max(take,nottake)
            return memo[(i,prev)]
        return f(n-1,False)
