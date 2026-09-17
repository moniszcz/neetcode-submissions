class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preceeding = {}
        succeeding = {}

        right_multiply, left_multiply = 1, 1
        for idx in range(len(nums)):
            right_multiply = right_multiply * nums[idx]
            preceeding[idx] = right_multiply
        
        for idx in range(len(nums) - 1, -1, -1):
            left_multiply = left_multiply * nums[idx]
            succeeding[idx] = left_multiply

        output = [succeeding[1]]

        for idx in range(1, len(nums) - 1):
            output.append(preceeding[idx - 1] * succeeding[idx + 1])
        
        output.append(preceeding[len(nums) - 2])
        
        return output
        