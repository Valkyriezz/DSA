class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        r=0
        n=len(s)
        count=0
        freq={"a":0,"b":0,"c":0}
        while r<n:
            freq[s[r]]+=1
            while freq["a"]>0 and freq["b"]>0 and freq["c"]>0:
                    freq[s[l]]-=1
                    l+=1
            count+=l
            r+=1
        return count