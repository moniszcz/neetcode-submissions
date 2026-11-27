"""
1. While loop Time O(nlogn)
2. Slow and fast pointers (cycle detection)

"""




class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquaredDigits(n: int) -> int:
            result = 0 
            while n:
                digit = n % 10
                result += digit * digit
                n = n // 10
            return result

        seen = set()
        while not (n == 1 or n in seen):
            seen.add(n)
            n = sumOfSquaredDigits(n)

        return n == 1
        
        