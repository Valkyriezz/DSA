class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen=0
        l=0
        r=0
        hashmap={}
        maxfreq=0
        n=len(s)
        while r<n:
            if s[r] in hashmap:
                hashmap[s[r]]+=1
            else:
                hashmap[s[r]]=1
            maxfreq=max(maxfreq,hashmap[s[r]])
            while (r-l+1)-maxfreq>k:
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
        