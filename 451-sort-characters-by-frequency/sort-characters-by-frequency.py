class Solution(object):
    def frequencySort(self, s):
        hashmap={}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        # return hashmap
        # sort hashmap
        st=sorted(hashmap.keys(),key=lambda x: hashmap[x],reverse=True)
        res=[]
        for i in st:
            res.append(i*hashmap[i])
        return "".join(res)