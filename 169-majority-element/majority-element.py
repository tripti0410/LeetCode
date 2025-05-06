class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1) Find a candidate
        candidate, count = None, 0
        for x in nums:
            if count == 0:
                candidate, count = x, 1
            elif x == candidate:
                count += 1
            else:
                count -= 1

        # 2) (Optional) Verify candidate
        #    If problem guarantees a majority exists, you can skip this.
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        # otherwise handle no-majority case if needed
        return -1
