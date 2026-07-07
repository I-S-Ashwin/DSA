class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0
        while n:
            digit = n % 10
            if digit != 0:
                x = x * 10 + digit
                digit_sum += digit
            n //= 10
        
        x = int(str(x)[::-1]) if x != 0 else 0
        
        return x * digit_sum
