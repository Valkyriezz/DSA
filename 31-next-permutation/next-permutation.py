class Solution(object):
    def nextPermutation(self, nums):
        ind=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind!=-1:
            for j in range(n-1,ind,-1):
                if nums[j]>nums[ind]:
                    nums[j],nums[ind]=nums[ind],nums[j]
                    break
        nums[ind+1:]=reversed(nums[ind+1:])    
        return nums   