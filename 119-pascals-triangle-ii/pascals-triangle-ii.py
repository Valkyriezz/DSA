class Solution(object):
    def getRow(self, rowIndex):
        res=[]
        ans=1
        res.append(ans)
        for i in range(1,rowIndex+1):
            ans=ans*(rowIndex-i+1)
            ans=ans//i
            res.append(ans)
        return res
        