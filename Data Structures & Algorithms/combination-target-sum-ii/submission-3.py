class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i,candidate,sub,ans,summ,target):
            if summ==target:
                if sorted(sub) not in ans:
                    ans.append(sorted(sub.copy()))
                return
            
            if i ==len(candidate):
                return


            for j in range(i,len(candidate)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                sub.append(candidate[j])
                summ+=candidate[j]
                if summ <=target:
                    helper(j+1,candidate,sub,ans,summ,target)
                summ-=sub[-1]
                sub.pop()



        candidates.sort
        sub,ans=[],[]
        summ=0
        helper(0,candidates,sub,ans,summ,target)
        return ans