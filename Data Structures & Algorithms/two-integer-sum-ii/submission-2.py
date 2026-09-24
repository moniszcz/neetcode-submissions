class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_target = target - numbers[left]

            if curr_target < numbers[right]:
                right -= 1
            elif curr_target > numbers[right]:
                left += 1
            else:
                return [left + 1, right + 1]
        