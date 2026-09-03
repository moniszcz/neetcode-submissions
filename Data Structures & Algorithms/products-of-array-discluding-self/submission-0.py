import math
class Solution:
    def multiply(self, nums, el_to_omit):
        product = 1
        for el_idx in range(len(nums)):
            if el_idx != el_to_omit:
                product *= nums[el_idx]
        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # dictionary_containing_elemes_of_list = {idx: el for idx, el in nums}
        list_to_return = [self.multiply(nums, i) for i in range(len(nums))]
        return list_to_return
        