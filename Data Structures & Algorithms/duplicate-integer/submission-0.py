class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=sorted(nums)
        for i,num in enumerate(x) :
            if(i !=len(x)-1 and num == x[i+1]):
                return True
        return False
        