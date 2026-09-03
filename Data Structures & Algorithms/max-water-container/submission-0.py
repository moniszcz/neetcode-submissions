class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l_pointer = 0
        r_pointer = len(heights) - 1

        while l_pointer < r_pointer:
            left_bar_height = heights[l_pointer]
            right_bar_height = heights[r_pointer]
            cur_area = (r_pointer - l_pointer) * min(right_bar_height, left_bar_height)
            max_area = max(max_area, cur_area)

            if left_bar_height < right_bar_height:
                l_pointer += 1
            elif right_bar_height > left_bar_height:
                r_pointer -= 1
            else:
                # edge case: bars are of equal height, no matter which pointer will be shifted:
                r_pointer -= 1


        return max_area 
        