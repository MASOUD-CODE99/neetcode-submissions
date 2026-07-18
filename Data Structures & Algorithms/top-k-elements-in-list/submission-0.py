class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans=[]
        for index, num in enumerate(nums):
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        while(k):
            mx = max(freq, key=freq.get)
            freq[mx]=-1
            ans.append(mx)
            k-=1
        return ans
            