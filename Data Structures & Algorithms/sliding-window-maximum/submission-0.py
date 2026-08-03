class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s=[]
        x=0
        ans=[]
        l=0

        for r in range(len(nums)):

            while s and nums[s[-1]] < nums[r] and r-s[-1] < k:
                s.pop()
            s.append(r)


            if r-l+1 == k:
            
                if s[x]<l:
                    x+=1

                l+=1 

                ans.append(nums[s[x]])

        return ans




        