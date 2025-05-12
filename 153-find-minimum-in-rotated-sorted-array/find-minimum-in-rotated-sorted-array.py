class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # Start with infinity so any number in the array will be smaller
        min_value = float('inf')
        
        # Continue while our window is valid
        while left <= right:
            mid = (left + right) // 2
            
            # Update the minimum if we find a smaller element
            if nums[mid] < min_value:
                min_value = nums[mid]
            
            # Decide which half is “rotated” and move pointers accordingly
            if nums[mid] >= nums[right]:
                # Minimum must lie to the right of mid
                left = mid + 1
            else:
                # Catch-all for the remaining case (also moves left boundary)
                right = mid - 1
        
        return min_value