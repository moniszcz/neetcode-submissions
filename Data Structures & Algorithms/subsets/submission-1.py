class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output_array = [[]]

        for num in nums:
            array_to_append = []
            for element in output_array:
                array_to_append.append(element + [num])
            output_array.extend(array_to_append)
        return output_array
        