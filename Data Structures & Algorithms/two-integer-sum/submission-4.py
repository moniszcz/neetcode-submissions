class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first solution
        # for i in range(len(nums)):
        #     curr_diff = target - nums[i]
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == curr_diff:
        #             return i, j
        difference_to_index = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in difference_to_index:
                return difference_to_index[nums[i]], i
            difference_to_index[diff] = i
            
