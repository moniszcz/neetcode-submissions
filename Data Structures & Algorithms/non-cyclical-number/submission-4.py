class Solution:
    def isHappy(self, n: int) -> bool:
        # slow and fast pointer - good when cycles need to be detected
        def sumOfDigits(n: int) -> int:
            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            return output

        
        slow, fast = n, sumOfDigits(n)

        while not (fast == 1 or slow == fast):
            slow = sumOfDigits(slow)
            fast = sumOfDigits(sumOfDigits(fast))
        
        return fast == 1
        