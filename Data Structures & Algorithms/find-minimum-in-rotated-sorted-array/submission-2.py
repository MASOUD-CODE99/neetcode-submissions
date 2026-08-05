class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        ans = float("inf")

        while r>=l:
            mid=(l+r)//2
            ans=min(ans,nums[mid])

            if nums[mid] >= nums[r] and nums[mid] >= nums[l]:
                l=mid+1

            elif nums[mid] <= nums[r] and nums[mid] <= nums[l]:
                r=mid-1

            else:
                r=mid-1
        return ans



        