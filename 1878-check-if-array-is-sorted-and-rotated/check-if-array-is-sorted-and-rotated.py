class Solution(object):
    def reverse(self,nums):
        return nums[::-1]
    def check(self, nums):
        index=-1
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                if index!=-1:
                    return False
                index=i
        #check from where it is sorted
        if index==-1:
            return True
        if nums[n-1]>nums[0]:
            return False
        return True


                
        