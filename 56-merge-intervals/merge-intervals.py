class Solution(object):
    def merge(self, nums):
        n=len(nums)
        nums.sort()
        res=[nums[0]]
        for x,(i,j) in enumerate(nums[1:]):
            last=res[-1]
            if last[1]>=i:
                last[1]=max(last[1],j)
            else:
                res.append([i,j])
        return res

            

        