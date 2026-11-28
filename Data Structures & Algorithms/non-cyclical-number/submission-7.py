"""
1. While loop until n == 1 or n was visited
Time complexity: O(logn) #each number has around log_10 n digits
Memory complexity: O(logn)

2. Fast and slow pointers
Time complexity: O(logn)
Memory complexity: O(1) - we don't allocate additional memory
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
        
        slow = n
        fast = sumOfSquaredDigits(n)
        while not (slow == fast or fast == 1):
            slow = sumOfSquaredDigits(slow)
            fast = sumOfSquaredDigits(sumOfSquaredDigits(fast))
        
        return fast == 1





