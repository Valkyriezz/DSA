class Solution(object):
    def singleNumber(self, nums):
        n=len(nums)
        # for i in range(n):
        #     num=nums[i]
        #     count=0
        #     for j in range(n):
        #         if num==nums[j]:
        #             count+=1
        #     if count==1:
        #         return num
        # hashmap={}
        # for i in range(n):
        #     if nums[i] in hashmap:
        #         hashmap[nums[i]]+=1
        #     else:
        #         hashmap[nums[i]]=1
        # for key,val in hashmap.items():
        #     if val==1:
        #         return key
        xor=0
        for i in range(n):
            xor=xor^nums[i]
        return xor
