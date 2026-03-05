class Solution(object):
    def rearrangeArray(self, nums):
        neg=1
        pos=0
        n=len(nums)
        arr=[0]*n
        for i in range(n):
            if nums[i]<0:
                arr[neg]=nums[i]
                neg+=2
            else:
                arr[pos]=nums[i]
                pos+=2
        return arr

        