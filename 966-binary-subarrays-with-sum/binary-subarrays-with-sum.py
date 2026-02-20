class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap={0:1}
        summ=0
        n=len(nums)
        k=goal
        count=0
        for i in range(n):
            summ+=nums[i]
            complement=summ-k
            if complement in hashmap:
                count+=hashmap[complement]
            if summ not in hashmap:
                hashmap[summ]=1
            else:
                hashmap[summ]+=1
        return count