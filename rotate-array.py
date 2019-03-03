from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        last = len(nums) - 1
        for i in range(0, k):
            nums.insert(0, nums.pop(last))
            