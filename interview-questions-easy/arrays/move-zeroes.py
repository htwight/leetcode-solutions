from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        nums[:] = [x for x in nums if x != 0]
        for zeros in range(count):
            nums.append(0)
