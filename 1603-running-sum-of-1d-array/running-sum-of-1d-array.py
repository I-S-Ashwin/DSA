class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            nums[i], nums[i+1] = nums[i], nums[i] + nums[i+1]
        return nums