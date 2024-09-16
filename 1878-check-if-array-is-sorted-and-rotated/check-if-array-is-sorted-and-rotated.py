class Solution:
    def check(self, nums: List[int]) -> bool:
        count, n = 0, len(nums)
        for i in range(0, n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
        if count > 1:
            return False
        return True
        
                