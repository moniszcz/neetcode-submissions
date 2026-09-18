class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for i in nums:
            if i - 1 not in nums_set:
                curr_len = 1
                while i + 1 in nums_set:
                    curr_len += 1
                    i += 1
                max_len = max(curr_len, max_len)
        
        return max_len

        