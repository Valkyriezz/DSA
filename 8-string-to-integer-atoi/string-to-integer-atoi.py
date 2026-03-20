class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        n=len(s)
        i=0
        sign=""
        num=[]
        if not s:
            return 0
        if i==0:
            if s[i]=="-" or s[i]=="+":
                sign=s[i]
                i+=1
        while i<n and s[i]=="0":
            i+=1
        while i<n and s[i].isdigit():
            num.append(s[i])
            i+=1
        newnum="".join(num)
        finalNum=0
        if newnum=="":
            return 0
        else:
            for digit in newnum:
                finalNum*=10
                finalNum+=int(digit)
        if(sign=='-'):
            finalNum=-finalNum
        # return finalNum
        if -2**31<=finalNum<=2**31-1:
            return finalNum
        else:
            if finalNum<-2**31:
                return -2**31
            else:
                return 2**31-1
            
            
        