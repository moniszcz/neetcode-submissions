class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_idx = dict()

        for idx, i in enumerate(nums):
            current_target = target - i
            if current_target in value_to_idx:
                return [value_to_idx[current_target], idx]
            else:
                value_to_idx[i] = idx
        

        