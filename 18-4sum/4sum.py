class Solution(object):
    def fourSum(self, nums, target):
        res=[]
        nums.sort()
        n=len(nums)
        # i and j will remain constant
        for i in range(n):
            for j in range(i+1,n):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    summ=nums[i]+nums[j]+nums[k]+nums[l]
                    if summ>target:
                        l-=1
                    elif summ<target:
                        k+=1
                    else:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        res.append(temp)
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
        return res
                

        