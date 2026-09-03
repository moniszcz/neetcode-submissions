class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        cur_subset = []
        def solve(i, cur_subset):
            if i == len(nums):
                result.append(cur_subset.copy())
                return
            cur_subset.append(nums[i])
            solve(i+1, cur_subset)
            cur_subset.pop()

            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i = i+1
            
            solve(i+1, cur_subset)

        solve(0, [])
        return result

