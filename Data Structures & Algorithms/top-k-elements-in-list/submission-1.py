class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for n in nums:
            num_to_freq[n] = 1 + num_to_freq.get(n, 0)
        num_to_freq_tup = list(num_to_freq.items())
        sorted_by_value_num_to_frew = sorted(num_to_freq_tup, key=lambda item : item[1], reverse=True)
        output_list = []
        for i in range(k):
            output_list.append(sorted_by_value_num_to_frew[i][0])
        return output_list

        