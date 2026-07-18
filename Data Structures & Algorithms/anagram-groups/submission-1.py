class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = sorted(strs, key=lambda w: ''.join(sorted(w)))
        ar = [''.join(sorted(word)) for word in arr]

        lst = []
        lst.append([arr[0]]) if arr else None

        for i in range(1, len(ar)):
            if ar[i] == ar[i-1]:
                lst[-1].append(arr[i])
            else:
                lst.append([arr[i]])
        return lst
