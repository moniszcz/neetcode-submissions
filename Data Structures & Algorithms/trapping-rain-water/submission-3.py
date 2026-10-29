class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [height[0]]
        max_right = [0]*len(height)
        max_right[-1] = height[-1]
        traped_water = 0
        
        for i in range(1, len(height)):
            curr_max = max(height[i], max_left[i-1])
            max_left.append(curr_max)

        for i in range(len(height) - 2, -1, -1):
            curr_max = max(height[i], max_right[i+1])
            max_right[i] = curr_max
        
        for i in range(len(height)):
            min_border = min(max_left[i], max_right[i])
            cnt = min_border - height[i]
            if cnt > 0:
                traped_water += cnt

        return traped_water
            