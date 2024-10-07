class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for each in s:
            if stack and stack[-1]+each in ["AB", "CD"]:
                stack.pop()
            else:
                stack.append(each)
        return len(stack)