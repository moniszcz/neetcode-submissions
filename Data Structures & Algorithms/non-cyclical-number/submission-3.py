class Solution:
    def isHappy(self, n: int) -> bool:
        # Time complecity
        # Memory complexity

        def sumOfDigits(n: int) -> int:
            result = 0
            while n:
                digit = n % 10 # returns last digit
                result += digit ** 2 # add squared digit
                n = n // 10 # drop last digit 
            return result
        
        seen = set() # 'in' operation in set is O(1)
        while not (n == 1 or n in seen):
            seen.add(n)
            n = sumOfDigits(n)

        return n == 1 