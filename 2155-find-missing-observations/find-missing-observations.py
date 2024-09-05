class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_val = (mean * (n + len(rolls))) - sum(rolls)
        dice = [i for i in range(1, 7)]
        if missing_val > 6*n or missing_val<n:
            return []
        val = missing_val // n
        result = [val] * n
        remainder = missing_val % n
        for i in range(remainder):
            result[i] += 1
        return result