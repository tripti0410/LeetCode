class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float('-inf')
        current_sum = 0
        for i, val in enumerate(nums):
            current_sum += val
            if current_sum > total:
                total = current_sum
            if current_sum < 0:
                current_sum = 0
        return total