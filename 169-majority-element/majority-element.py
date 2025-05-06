class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) / 2
        num_count = {}
        for i in range(0, len(nums)):
            num_count[nums[i]] = num_count.get(nums[i], 0) + 1
            if num_count.get(nums[i]) and num_count[nums[i]] >= threshold:
                return nums[i]