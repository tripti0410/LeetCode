class Solution:
    def romanToInt(self, s: str) -> int:
        self.s=s
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value=0
        for i in range(len(s)):
            if i!= len(s)-1:
                if dict[s[i]]<dict[s[i+1]]:
                    value=value-dict[s[i]]
                else:
                    value=value+dict[s[i]]
            else:
                    value=value+dict[s[i]]
        return value 