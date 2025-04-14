class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str_map = {}
        def is_already_mapped(value):
            for each in str_map:
                if str_map[each] == value:
                    return True
            return False

        for i in range(len(s)):
            if not str_map.get(s[i]):
                if not is_already_mapped(t[i]):
                    str_map[s[i]] = t[i]
                else:
                    return False
            elif str_map[s[i]] != t[i]:
                return False

        return True