class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while r>=l:
            mid=(r+l)//2
            time_on_curr=0
            for pan in piles:
                time_on_curr+= math.ceil(pan/mid)
            if h>=time_on_curr:
                r=mid-1
                res=mid
            else:
                l=mid+1
        return res


        