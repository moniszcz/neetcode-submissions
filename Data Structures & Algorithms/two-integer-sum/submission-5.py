class Solution:
    #Time complexity O(n) - iterating through list; Memo complexity o(n) - builiding hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_to_index = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in difference_to_index:
                return difference_to_index[nums[i]], i
            difference_to_index[diff] = i
            
