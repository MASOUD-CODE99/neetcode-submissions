class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def fun(mid):
            hh=0
            for x in piles:
                hh+=(x + mid - 1) // mid
            return hh



        ans=0
        high=max(piles)
        low=1

        while high>=low:
            mid=(high+low)//2
            x=fun(mid)
            if x>h:
                low=mid+1
            else:
                high=mid-1
                ans=mid


        return ans