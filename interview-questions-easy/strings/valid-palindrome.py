import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-z0-9]|\s", "", s, flags=re.IGNORECASE).upper()
        return s == s[::-1]