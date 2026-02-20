class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # hashmap={0:1}
        # summ=0
        n=len(nums)
        # k=goal
        # count=0
        # for i in range(n):
        #     summ+=nums[i]
        #     complement=summ-k
        #     if complement in hashmap:
        #         count+=hashmap[complement]
        #     if summ not in hashmap:
        #         hashmap[summ]=1
        #     else:
        #         hashmap[summ]+=1
        # return count
        def f(goal):
            if goal<0:
                return 0
            l=0
            r=0
            summ=0
            count=0
            while r<n:
                summ+=nums[r]
                while summ>goal:
                    summ-=nums[l]
                    l+=1
                count+=r-l+1
                r+=1
            return count
        return f(goal)-f(goal-1)
