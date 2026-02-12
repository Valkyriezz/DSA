class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(piles,mid):
            hours=0
            n=len(piles)
            for i in range(n):
                hours+=math.ceil(piles[i]/mid)
            return hours
        maxi=max(piles)
        l=1
        r=maxi
        while l<=r:
            mid=(l+r)//2
            total=f(piles,mid)
            if total<=h:
                r=mid-1
            else:
                l=mid+1
        return l