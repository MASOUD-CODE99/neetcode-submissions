class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[0] * len(nums)
        post=[0] * len(nums)
        ans=[0] * len(nums)
        total=1
        for i in range(len(nums)):
            total *= nums[i]
            pre[i] = total
        total=1
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            post[i] = total
        
        for i in range(len(nums)):
            if i ==0:
                ans[i]=post[1]
            elif i ==len(nums)-1:
                ans[i]=pre[i-1]
            else:
                ans[i]=pre[i-1]*post[i+1]
        return ans
        