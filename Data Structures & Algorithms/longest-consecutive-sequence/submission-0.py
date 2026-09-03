class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_cons_seq = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr_length = 1
                while num + 1 in nums_set:
                    curr_length += 1
                    num += 1
                longest_cons_seq = max(curr_length, longest_cons_seq)
        return longest_cons_seq
