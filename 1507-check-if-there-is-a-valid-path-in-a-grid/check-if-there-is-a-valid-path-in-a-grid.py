class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        queue=deque()
        #put initital
        queue.append((0,0))
        # explore
        # how can we explore path 1,2,3,4,5,6 
        # can we find a relation ? 1 adjacent should be either 3 4 5 and 6
        # 2-> 3 4 5 6
        # 3-> 1 2 4 5 6
        # 4-> 1 2 3 5 6
        # 5-> 1 2 3 4 6
        # 6-> 1 2 3 4 5
        # now we can move 
        # right,left,down up
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        mappings={1:[(1,3,5),(1,4,6),(),()],   
                2:[(),(),(2,5,6),(2,3,4)],
                3:[(),(1,4,6),(2,5,6),()],
                4:[(1,3,5),(),(2,5,6),()],
                5:[(),(1,4,6),(),(2,3,4)],
                6:[(1,3,5),(),(),(2,3,4)]}
        visited=set()
        visited.add((0,0))
        while queue:
            x,y=queue.popleft()
            if x==n-1 and y==m-1:
                return True
            currdirection=grid[x][y]
            for i,(dx,dy) in enumerate(directions):
                nx=dx+x
                ny=dy+y
                if 0<=nx<n and 0<=ny<m:
                    if (nx,ny) not in visited:
                        if grid[nx][ny] in mappings[currdirection][i]:
                            queue.append((nx,ny))
                            visited.add((nx,ny))
        return False


                            