from collections import deque
class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        num = abs(x)
        queue = deque([])
        while (num != 0):
            queue.append(num % 10)
            num = num // 10

        result = 0
        base = [10**x for x in range(len(queue))]
        for power in base:
            result = result + queue.pop() * power

        if result > 2**31 - 1 or result < -(2**31):
            return 0
        else:
            return -result if negative else result
