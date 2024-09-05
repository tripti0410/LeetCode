class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        result = []
        missing_val = (mean * (n + len(rolls))) - sum(rolls)
        dice = [i for i in range(1, 7)]
        if missing_val > 6*n or missing_val<n:
            return []
        while n:
            val = min(6, missing_val-n+1)
            result.append(val)
            missing_val -= val
            n -= 1
        return result