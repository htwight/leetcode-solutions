# Admittedly, I did not come up with a solution that
# does not require extra memory. The XOR wasn't my idea.
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num

        return single
