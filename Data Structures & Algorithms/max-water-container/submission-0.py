class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa=0
        l=0
        r=len(heights)-1
        while(l<r):
            nowa=min(heights[r],heights[l])*(r-l)
            maxa=max(maxa,nowa)
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1

        return maxa