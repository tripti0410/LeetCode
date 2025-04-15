class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedsum = n * (n + 1) // 2
        actualsum = 0
        for i in range(n):
            actualsum += nums[i]
        return expectedsum - actualsum