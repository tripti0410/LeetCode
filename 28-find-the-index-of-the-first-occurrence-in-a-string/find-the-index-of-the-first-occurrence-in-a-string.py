class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Add edge cases
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
            
        n = 0  # needle index
        h = 0  # haystack index
        
        while h < len(haystack):
            if haystack[h] == needle[n]:
                # Store the potential starting position when we find first match
                if n == 0:
                    start_pos = h
                n += 1
                h += 1
                
                # If we've matched the entire needle, return the starting position
                if n == len(needle):
                    return start_pos
            else:
                # If we were in the middle of a match, reset and start from next position
                if n > 0:
                    h = h - n + 1  # Move back to position after last start
                    n = 0
                else:
                    h += 1
                    
        return -1
