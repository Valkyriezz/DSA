class Solution(object):
    def generate(self, numRows):
        res=[]
        def functionNCR(row,col):
            ans=1
            for i in range(col):
                ans=ans*(row-i)
                ans=ans//(i+1)
            return ans
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                temp.append(functionNCR(i,j))
            res.append(temp)
        return res

        