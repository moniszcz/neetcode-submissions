class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, subset):
            if i >= len(nums) or sum(subset) > target:
                return
            if sum(subset) == target:
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i, subset)

            subset.pop()

            dfs(i+1, subset)

            return
        
        dfs(0,[])
        return result
        