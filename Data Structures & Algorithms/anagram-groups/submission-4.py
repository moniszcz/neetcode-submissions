class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_orig = defaultdict(list)

        for i in strs:
            sorted_i = "".join(sorted(i))
            sorted_to_orig[sorted_i].append(i)
        
        return list(sorted_to_orig.values())