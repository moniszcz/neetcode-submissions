class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        curr_max_left, curr_max_right = 0, 0
        trapped = 0

        while left < right:
            if height[left] < height[right]:
                curr_max_left = max(curr_max_left, height[left])
                left += 1
                if curr_max_left > height[left]:
                    trapped += curr_max_left - height[left]
            else:
                curr_max_right = max(curr_max_right, height[right])
                right -= 1
                if curr_max_right > height[right]:
                    trapped += curr_max_right - height[right]
        
        return trapped
        