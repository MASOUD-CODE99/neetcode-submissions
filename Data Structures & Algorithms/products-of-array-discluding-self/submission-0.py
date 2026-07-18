class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=nums[:]
        l=nums[:]
        x=[]
        for i in range(1,len(r)):
            r[i]*=r[i-1]
        for i in range(len(l)-2,-1,-1):
            l[i]*=l[i+1]


        for index,i in enumerate(nums):
            if index==0:
                x.append(l[1])
            elif index==len(nums)-1:
                x.append(r[len(r)-2])
            else:
                x.append(l[index+1]*r[index-1])
        
        return x




       