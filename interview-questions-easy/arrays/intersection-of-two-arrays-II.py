# just gonna do the O(m * n) solution
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    nums2.remove(num1)
                    result.append(num1)
                    break
        return result