class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preceeding = {0: 1}
        succeeding = {len(nums) - 1 : 1}

        for idx in range(1, len(nums)):
            preceeding[idx] = preceeding[idx - 1] * nums[idx - 1]
        
        for idx in range(len(nums) - 2, -1, -1):
            succeeding[idx] = succeeding[idx + 1] * nums[idx + 1]

        output = []

        for idx in range(len(nums)):
            output.append(preceeding[idx] * succeeding[idx])
        
        return output
        