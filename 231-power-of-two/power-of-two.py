class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False 
        n=bin(n)
        num=n[2:]
        print(num)
        flag=None
        if num=="1":
            return True
        if num[0]=="1":
            flag=True
            for i in range(1,len(num)):
                if num[i]!="0":
                    flag=False
        return flag