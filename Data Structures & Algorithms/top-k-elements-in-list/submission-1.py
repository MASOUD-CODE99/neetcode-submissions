class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis=[]
        d={}
        nums.sort()
        times=0
        for i in range(len(nums)):
            times+=1
            if i==len(nums)-1 or nums[i] != nums[i+1]:
                d[nums[i]]=times
                times=0
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))        
        for key in d:
            lis.append(key)
            k-=1
            if k==0:
                return lis

