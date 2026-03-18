class Solution(object):
    def removeOuterParentheses(self, s):
        count=0
        n=len(s)
        res=""
        for i in range(n):
            if s[i]=="(":
                if count>0:
                    res+="("
                count+=1
            else:
                count-=1
                if count>0:
                    res+=")"
        return res
                