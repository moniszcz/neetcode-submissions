class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preceeding = {0: 1}
        succeeding = {len(nums) - 1 : 1}

        right_multiply, left_multiply = 1, 1
        for idx in range(1, len(nums)):
            right_multiply = right_multiply * nums[idx - 1]
            preceeding[idx] = right_multiply
        
        for idx in range(len(nums) - 2, -1, -1):
            left_multiply = left_multiply * nums[idx + 1]
            succeeding[idx] = left_multiply

        output = []

        for idx in range(len(nums)):
            output.append(preceeding[idx] * succeeding[idx])
        
        return output
        