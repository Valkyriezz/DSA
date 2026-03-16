class Solution(object):
    def trap(self, height):
        n=len(height)
        total=0
        lmax=0
        rmax=0
        l=0
        r=n-1
        while l<r:
            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])
            if lmax<rmax:
                total+=lmax-height[l]
                l+=1
            else:
                total+=rmax-height[r]
                r-=1
        return total        