class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openp, closep = 0, 0
        for each in s:
            if each == '(':
                openp += 1
            elif each == ')':
                if openp > 0:
                    openp -= 1
                else:
                    closep += 1
        return openp + closep