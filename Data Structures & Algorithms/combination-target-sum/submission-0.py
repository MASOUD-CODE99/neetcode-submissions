class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def helper(i, nums, subset, curset,target,summ):
            if target == summ:
                subset.append(curset.copy())
                return

            if i == len(nums):
                return

            for j in range(i,len(nums)):
                curset.append(nums[j])
                summ+=nums[j]
                if summ<=target:
                    helper(j,nums,subset,curset,target,summ)
                summ-=curset[-1]
                curset.pop()






        nums.sort()
        subset, curset = [], []
        summ=0
        helper(0, nums, subset, curset,target,summ)
        return subset
