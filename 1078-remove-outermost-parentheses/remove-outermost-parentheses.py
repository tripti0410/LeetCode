class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        new_str = ''
        for each in s:
            if each == '(':
                if count > 0:
                    new_str += '('
                count += 1
            else:
                count -= 1
                if count > 0:
                    new_str += ')'
        return new_str             