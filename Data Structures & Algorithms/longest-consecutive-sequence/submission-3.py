class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        lst=sorted(list(num_set))

        longe=0
        ans=0

        for i in range(1,len(lst)):
            if lst[i]==lst[i-1]+1:
                longe+=1
            else:
                longe=0
            ans=max(ans,longe)
        return ans+1 




