class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        rank=[0]*n
        parent=[i for i in range(n)]
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx==rooty:
                return 
            # unite
            if rank[rootx]>rank[rooty]:
                parent[rooty]=parent[rootx]
            elif rank[rootx]<rank[rooty]:
                parent[rootx]=parent[rooty]
            else:
                parent[rootx]=rooty
                rank[rooty]+=1
        hashmap={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] in hashmap:
                    pass
                else:
                    hashmap[accounts[i][j]]=i
        # print(hashmap)
        for i in range(n):
            for j in range(1,len(accounts[i])):
                union(i,hashmap[accounts[i][j]])
        groups={}
        for email,ind in hashmap.items():
            root=find(ind)
            if root not in groups:
                groups[root]=[]
            groups[root].append(email)
            
        res=[]
        for root,emails in groups.items():
            # print(root,email)
            name=accounts[root][0]
            res.append([name]+sorted(emails))
        return res

                    

                