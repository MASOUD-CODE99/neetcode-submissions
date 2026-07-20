class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, x in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < x:
                j = stack.pop()
                result[j] = i-j

            stack.append(i)

        return result