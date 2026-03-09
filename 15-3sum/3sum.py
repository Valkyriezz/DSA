class Solution(object):
    def threeSum(self, nums):
        res=[]
        nums.sort()
        n=len(nums)
        # i will remain constant
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                summ=nums[i]+nums[j]+nums[k]
                if summ>0:
                    k-=1
                elif summ<0:
                    j+=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    res.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res
                
