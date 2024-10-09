class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for each in s:
            if each == '(':
                stack.append(each)
            elif each == ')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(')')
        return len(stack)