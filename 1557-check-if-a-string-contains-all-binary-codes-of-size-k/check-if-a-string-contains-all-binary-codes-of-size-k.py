class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        sets=set()
        for i in range(n-k+1):
            curr=s[i:i+k]
            sets.add(curr)
        if len(sets)==(1<<k):
            return True
        else:
            return False
            




        