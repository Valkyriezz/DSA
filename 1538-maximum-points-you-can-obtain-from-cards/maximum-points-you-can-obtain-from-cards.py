class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        lsum=0
        rsum=0
        maxsum=0
        while l<k:
            lsum+=nums[l]
            l+=1
        maxsum=max(lsum,maxsum)
        for i in range(k):
            # l-=1
            lsum-=nums[k-1]
            rsum+=nums[r]
            r-=1
            k-=1
            maxsum=max(lsum+rsum,maxsum)
        return maxsum


        