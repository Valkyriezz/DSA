class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi=0
        n=len(nums)
        count=0
        for i in range(n):
            if nums[i]==1:
                count+=1
            else:
                count=0
            maxi=max(maxi,count)
        return maxi