class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        hashmap={}
        n=len(nums2)
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack==[]:
                hashmap[nums2[i]]=-1
            else:
                hashmap[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        ans=[]
        for i in range(len(nums1)):
            curr=nums1[i]
            ans.append(hashmap[curr])
        return ans
                    
        
        