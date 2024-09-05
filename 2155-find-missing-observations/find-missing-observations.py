class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_val = (mean * (n + len(rolls))) - sum(rolls)
        if missing_val > 6*n or missing_val<n:
            return []
        val = missing_val // n
        result = [0] * n
        remainder = missing_val % n
        for i in range(remainder):
            result[i] = val + 1
        for i in range(remainder, n):
            result[i] = val
        return result