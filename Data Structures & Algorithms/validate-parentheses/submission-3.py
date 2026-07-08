class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        tracker = []
        for char in s:

            if char in paren_map:
                if not tracker or tracker.pop() != paren_map[char]:
                    return False
            else:
                tracker.append(char)
            
        return not tracker