class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for idx, value in enumerate(nums):
            if idx > 0 and nums[idx - 1] == value:
                continue
            if value > 0:
                break
            
            l_pointer = idx + 1
            r_pointer = len(nums) - 1
            
            while l_pointer < r_pointer:
                cur_sum = value + nums[l_pointer] + nums[r_pointer]
                if cur_sum > 0:
                    r_pointer -= 1
                elif cur_sum < 0:
                    l_pointer += 1
                else:
                    result.append([value, nums[l_pointer], nums[r_pointer]])
                    l_pointer += 1
                    while nums[l_pointer - 1] == nums[l_pointer] and l_pointer < r_pointer:
                        l_pointer += 1
        
        return result


        