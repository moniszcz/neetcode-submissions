class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #[array_idx, temp]
        for idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > stack[-1][1]:
                stack_id, stack_temp = stack.pop()
                result[stack_id] = idx - stack_id
            stack.append([idx, curr_temp])
        return result