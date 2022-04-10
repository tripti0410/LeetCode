# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class Solution:
  # Solution 1 (Time Complexity = O(n^2))
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                res=nums[i]+nums[j]
                if(res==target):
                    array=[i,j]
                    
                    print(array)

  # Solution 2 (Time Complexity = O(n))
    def twoSum2(self, nums: list[int], target: int) -> list[int]:

      a={}
      for i, val in enumerate(nums):
          if target-val in a:
              print([a[target-val],i])
          else:
              a[val]=i

a=Solution()
a.twoSum([3,2,4],6)
a.twoSum2([2,7,11,15],9)


      