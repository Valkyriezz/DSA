class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #1010
        #0111
        start=bin(start)[2:]
        # print(start)
        goal=bin(goal)[2:]
        n=len(start)
        m=len(goal)
        def makelenequal(n,m):
            nonlocal start,goal
            if n==m:
                return 
            if n>m:
                for i in range(n-m):
                    goal="0"+goal
            if m>n:
                for i in range(m-n):
                    start="0"+start
        makelenequal(n,m)
        print(start)
        print(goal)
        n=len(start)
        m=len(goal)
        count=0
        for i in range(n-1,-1,-1):
            if i<m:
                if start[i]!=goal[i]:
                    count+=1
                else:
                    continue
        return count

