class Solution(object):
    def isIsomorphic(self, s, t):
        hashmap={}
        used=set()
        n=len(s)
        if len(t)!=n:
            return False
        l=0
        r=0
        while l<n and r<n:
            if s[l] in hashmap:
                if hashmap[s[l]]!=t[r]:
                    return False
            else:
                if t[r] in used:
                    return False
                else:
                    hashmap[s[l]]=t[r]
                    used.add(t[r])
            l+=1
            r+=1
        return True

        