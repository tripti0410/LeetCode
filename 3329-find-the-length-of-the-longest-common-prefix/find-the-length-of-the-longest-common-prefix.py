class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max_len = 0
        prefix_sum = {}
        for num in arr1:
            val = ''
            for each in str(num):
                val += each
                prefix_sum[val] = prefix_sum.get(val, 0) + 1

        for num in arr2:
            val = ''
            for each in str(num):
                val += each
                if val in prefix_sum:
                    max_len = max(max_len, len(val))
        return max_len