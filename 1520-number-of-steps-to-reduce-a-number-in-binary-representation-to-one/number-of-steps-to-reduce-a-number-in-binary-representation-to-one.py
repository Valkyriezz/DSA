class Solution:
    def numSteps(self, s: str) -> int:
        s=list(s)
        def addOne(binary):
            carry=0
            n=len(binary)
            for i in range(n-1,-1,-1):
                if binary[i]=="1":
                    carry=1
                    binary[i]="0"
                else:
                    if carry==0:
                        break
                    else:
                        binary[i]="1"
                        carry=0
                        break
            # if carry is one, add extra 1 to the left
            if carry==1:
                binary.insert(0,"1")
        count=0 
        while True:
            if s==["1"]:
                return count
            count+=1
                # either odd or even
            if s[-1]=="0":
                #means it is even
                s.pop()
                # print(s)
            else:
                addOne(s)
        return count 
                    
                    
            
            
        