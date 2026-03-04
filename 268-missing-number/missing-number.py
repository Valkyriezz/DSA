class Solution(object):
    def missingNumber(self, nums):
        # n=len(nums)
        # totalsum=(n*(n+1))//2
        # currsum=0
        # for i in range(n):
        #     currsum+=nums[i]
        # return totalsum-currsum
        n=len(nums)
        xor=n
        for i in range(n):
            xor^=i^nums[i]
        return xor
        