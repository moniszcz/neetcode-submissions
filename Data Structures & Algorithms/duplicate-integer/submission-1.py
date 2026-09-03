class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            if frequency[n] > 1:
                return True
        return False
        