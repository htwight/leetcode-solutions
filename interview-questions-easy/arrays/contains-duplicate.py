from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = []
        for num in nums:
            if num in found:
                return True
            else:
                found.append(num)
        return False

class BetterSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
