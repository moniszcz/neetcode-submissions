# O(nlogn) solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_to_freq[n] = 1 + num_to_freq.get(n, 0)

        for num, count in num_to_freq.items():
            freq[count].append(num)

        results = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                results.append(n)
                if len(results) == k:
                    return results
        
        