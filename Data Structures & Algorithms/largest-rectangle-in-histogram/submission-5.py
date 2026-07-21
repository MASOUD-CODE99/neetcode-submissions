class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (index, height)
        max_area = 0

        for i, h in enumerate(heights):

            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                width = i - index
                max_area = max(max_area, height * width)

                start = index

            stack.append((start, h))

        # Treat the end as a smaller height: 0
        for index, height in stack:
            width = len(heights) - index
            max_area = max(max_area, height * width)

        return max_area