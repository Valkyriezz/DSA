class Solution(object):
    def subArrayRanges(self, nums):
        # mod=10**9+7
        n=len(nums)
        total=0
        for i in range(n):
            mini=float("inf")
            maxi=float("-inf")
            for j in range(i,n):
                mini=min(mini,nums[j])
                maxi=max(maxi,nums[j])
                diff=maxi-mini
                total=(total+diff)
        return total
        