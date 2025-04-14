class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_2_t = {}
        t_2_s = {}
        for i in range(len(s)):
            if not s_2_t.get(s[i]):
                if not t_2_s.get(t[i]):
                    s_2_t[s[i]] = t[i]
                    t_2_s[t[i]] = s[i]
                else:
                    return False
            elif s_2_t[s[i]] != t[i]:
                return False

        return True