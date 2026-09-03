class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset_to_add = []

        def dfs(idx):
            if idx >= len(nums):
                output.append(subset_to_add.copy())
                return
            
            #Add next element:
            subset_to_add.append(nums[idx])
            dfs(idx + 1)

            #Pop last element (add empty):
            subset_to_add.pop(-1)
            dfs(idx + 1)
        
        
        dfs(0)
        return output
        