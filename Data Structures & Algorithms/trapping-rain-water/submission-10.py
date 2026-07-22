class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        area=0
        l = 0

        for r in range(len(height)):
            if height[r]>=height[l]:
                ans+=area
                area=0
                l=r
            else:
                area+=height[l]-height[r]


        height.reverse()

        area=0
        l = 0

        for r in range(len(height)):
            if height[r]>height[l]:
                ans+=area
                area=0
                l=r
            else:
                area+=height[l]-height[r]


        return ans

         