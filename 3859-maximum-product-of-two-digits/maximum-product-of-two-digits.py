class Solution:
    def maxProduct(self, n: int) -> int:
        n = sorted(list(map(int, str(n))))
        return n[-2] * n[-1]
