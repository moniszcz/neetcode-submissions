class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and right pointer solution
        # Time O(logn) - bc at each step half of the array is discarded
        # Memory O(1)

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2
            if target > nums[mid_index]:
                left = mid_index + 1
            elif target < nums[mid_index]:
                right = mid_index - 1
            else:
                return mid_index
        
        return -1
        
        