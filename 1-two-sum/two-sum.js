/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hash_map = {}
    for(let i=0; i<nums.length; i++)
    {
        let value = target - nums[i]
        if(hash_map[value] !== undefined)
        {
            return [hash_map[value], i]
        }
        else
        {
            hash_map[nums[i]] = i
        }
    }
};