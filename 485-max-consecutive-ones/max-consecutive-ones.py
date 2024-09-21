class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, max_len = 0, 0
        for right in range(len(nums)):
            if nums[right] == 1:
                curr += 1
            else:
                curr = 0
            max_len = max(max_len, curr)
        return max_len