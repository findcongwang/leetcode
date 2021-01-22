class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = (s+" EOL").split()
        if len(words) == 1:
            return 0
        return len(words[-2])