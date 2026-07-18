class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        res=[]
        while r>l:
            if numbers[l]+numbers[r]>target:
                if numbers[r]>numbers[l]:
                    r-=1
                else:
                    l+=1
            elif numbers[l]+numbers[r]<target:
                if numbers[r]>numbers[l]:
                    l+=1
                else:
                    r-=1
            else:
                res.append(l+1)
                res.append(r+1)
                return res
        
        