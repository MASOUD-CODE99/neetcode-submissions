class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        

        while r!=l+1 and len(nums)!=1:
            mid=(r+l)//2
            if nums[mid]<nums[r]:
                if target>=nums[mid] and target<=nums[r]:
                    l=mid
                else:
                    r=mid
            else:
                if target>=nums[l] and target<=nums[mid]:
                    r=mid
                else:
                    l=mid
        if target==nums[r]:
            return r
        elif target==nums[l]:
            return l
        else:
            return -1


  
        