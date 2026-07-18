class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pr={}
        for i,num in enumerate(nums):
            df=target-num
            if df in pr :
                return [pr[df],i]
            pr[num]=i


