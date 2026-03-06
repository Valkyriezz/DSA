class Solution(object):
    def longestConsecutive(self, nums):
        if nums==[]:
            return 0
        sets=set(nums)
        count=0
        for i in sets:
            if i-1 not in sets:
                curr=1
                while i+curr in sets:
                    curr+=1
                count=max(curr,count)
        return count

        