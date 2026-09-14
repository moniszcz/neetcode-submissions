class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freqs = defaultdict(int)
        # result = [[]] * len(nums) In Python, using [[]] * n does not create n independent empty lists. Instead, it creates a single outer list containing n references to the exact same inner list object in memory.
        result = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freqs[n] += 1
        
        for key, value in freqs.items():
            result[value].append(key)
        
        output = []
        for i in range(len(result) - 1, 0, -1):
            for num in result[i]:
                output.append(num)
                if len(output) == k:
                    return output



        
