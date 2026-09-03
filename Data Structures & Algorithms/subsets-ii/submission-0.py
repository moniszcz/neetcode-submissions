class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        cur_subset = []

        def dfs(i):
            if i >= len(nums):
                sorted_cur_subset = sorted(cur_subset.copy())
                if not sorted_cur_subset in results:
                    results.append(sorted_cur_subset)
                return
            
            cur_subset.append(nums[i])
            dfs(i+1)
            cur_subset.pop(-1)
            dfs(i+1)

        dfs(0)
        return results
        