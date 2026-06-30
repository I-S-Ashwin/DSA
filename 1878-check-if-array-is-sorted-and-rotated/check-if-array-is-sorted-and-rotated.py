class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        count = 0
        for i in range(l):
            if nums[i] > nums[(i+1)%l]:
                count+=1
                if count > 1:
                    return False
        return True