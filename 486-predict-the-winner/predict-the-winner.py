class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
    
        memo = {}
    
        def dp(l, r):
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]
            
            pick_left = nums[l] - dp(l+1, r)
            pick_right = nums[r] - dp(l, r-1)
            
            memo[(l, r)] = max(pick_left, pick_right)
            return memo[(l, r)]
        
        return dp(0, n-1) >= 0