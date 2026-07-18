class Solution:
    def findMin(self, nums: List[int]) -> int:
        r,l=len(nums)-1,0
        mid=(r+l)//2
        if nums[r]>=nums[mid] and nums[l]<=nums[mid]:
            return nums[0]

        

        while r!=l+1:
            mid=(r+l)//2
            if nums[mid] > nums[r]:
                l=mid
            elif nums[mid] < nums[l]:
                r=mid
        
        return nums[l] if nums[r]>nums[l] else nums[r]


                

        