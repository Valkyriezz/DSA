class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        n=len(s)
        count=0
        # stack=[]
        for i in range(n):
            if s[i]=="(":
                count+=1
                maxi=max(count,maxi)
            elif s[i]==")":
                count-=1
        return maxi