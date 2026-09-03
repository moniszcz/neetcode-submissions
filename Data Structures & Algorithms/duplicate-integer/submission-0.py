class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         set_of_nums = set(nums)
         if len(set_of_nums) != len(nums):
            return True
         return False