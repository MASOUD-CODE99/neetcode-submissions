class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        sum=0
        r=1
        while(n>r):
            if prices[r]-prices[l] <= 0:
                l=r
                r+=1
            else:
                sum=max(prices[r]-prices[l],sum)
                r+=1
        return sum
