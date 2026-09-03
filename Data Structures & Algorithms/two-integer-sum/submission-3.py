class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first solution
        for i in range(len(nums)):
            curr_diff = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == curr_diff:
                    return i, j
