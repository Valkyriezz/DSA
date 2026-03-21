class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0 or n%2==1:
            return False 
        while(n>0):
            if(n==1): return True
            if(n%2==1): return False
            n=n>>1
        return True
            
        