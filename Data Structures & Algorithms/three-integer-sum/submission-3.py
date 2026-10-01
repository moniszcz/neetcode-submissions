class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, output = 0, set()
        while i< len(nums) - 1 and nums[i] <= 0:
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum > - nums[i]:
                    right -= 1
                elif current_sum < - nums[i]:
                    left += 1
                else:
                    candidate = [nums[i], nums[left], nums[right]]
                    output.add(tuple(candidate))
                    right -= 1
            i += 1

        return list(output)    
        