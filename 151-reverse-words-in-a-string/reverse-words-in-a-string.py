class Solution(object):
    def reverseWords(self, s):
        # eht         eulb
        def remove(s):
            start=0
            end=len(s)-1
            while start<=end and s[start]==" ":
                start+=1
            while end>=start and s[end]==" ":
                end-=1
            return s[start:end+1]
        def reverse(s):
            return s[::-1]
        s=remove(s)
        s=reverse(s)
        n=len(s)
        ans=""
        i=0
        while i<n:
            word=""
            while i<n and s[i]==" ":
                i+=1
            while i<n and s[i]!=" ":
                word+=s[i]
                i+=1
            word=reverse(word)
            if len(word)>0:
                if ans=="":
                    ans=word
                else:
                    ans=ans+" "+word
        return ans