class Solution(object):
    def romanToInt(self, s):
        n=len(s)
        num=0
        hashmap={
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000
        }  
        if n<=1:
            return hashmap[s]
        for i in range(n-1):
            if hashmap[s[i]]<hashmap[s[i+1]]:
                num-=hashmap[s[i]]
            else:
                num+=hashmap[s[i]]
        num+=hashmap[s[n-1]]
        return (num)
        