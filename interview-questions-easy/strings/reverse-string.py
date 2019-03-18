from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = [s[i] for i in range(len(s) - 1, -1, -1)]

class PythonSolution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]