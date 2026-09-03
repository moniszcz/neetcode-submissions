class Solution:
    def trap(self, height: List[int]) -> int:
        l_pointer = 0 
        r_pointer = len(height) - 1
        trapped_water_sum = 0

        # we care about max boundaries as they are making vessels
        l_max = height[l_pointer]
        r_max = height[r_pointer]

        while l_pointer < r_pointer:
            # including equality, because in such case it doesn't matter which pointer will be reassigned
            if l_max <= r_max:
                trapped_water_sum += l_max - height[l_pointer]
                l_pointer += 1
                l_max = max(l_max, height[l_pointer])
            else:
                trapped_water_sum += r_max - height[r_pointer]
                r_pointer -= 1
                r_max = max(r_max, height[r_pointer])
        
        return trapped_water_sum
        