class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            # Calculate current area
            width = r - l
            current_area = width * min(heights[l], heights[r])
            max_water = max(max_water, current_area)

            # Move the pointer at the shorter bar
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water