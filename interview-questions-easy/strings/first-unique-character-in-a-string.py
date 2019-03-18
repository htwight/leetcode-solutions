class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = 0

        for c in s:
            counts[c] += 1

        for c in counts:
            if counts[c] == 1:
                return s.find(c)
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("lovelevettcodecd"))