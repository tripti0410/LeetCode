/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let count = 0;
    let maxCount = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // extend the current streak
            count++;
            // record if it's the longest so far
            if (count > maxCount) {
                maxCount = count;
            }
        } else {
            // streak broken by a zero → reset count
            count = 0;
        }
    }

    return maxCount;
};