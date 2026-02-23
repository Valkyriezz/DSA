class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l=0
        r=0
        n=len(s)
        sets=set()
        while r<n:
            if r-l+1<k:
                r+=1
            elif r-l+1>k:
                l+=1
            else:
                sets.add(s[l:r+1])
                r+=1
                l+=1
        if len(sets)==2**k:
            return True
        else:
            return False
        






        