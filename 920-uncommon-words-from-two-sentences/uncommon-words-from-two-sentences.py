class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_count, s2_count = {}, {}
        result = []
        for each in s1.split(' '):
            s1_count[each] = s1_count.get(each, 0) + 1
        
        for each in s2.split(' '):
            s2_count[each] = s2_count.get(each, 0) + 1

        for each in s1_count:
            if not s2_count.get(each):
                if s1_count.get(each) < 2:
                    result.append(each)
        
        for each in s2_count:
            if not s1_count.get(each):
                if s2_count.get(each) < 2:
                    result.append(each)

        return result