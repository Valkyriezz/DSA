class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=nums[0]
        n=len(nums)
        for i in range(1,n):
            xor^=nums[i]
        return xor

        