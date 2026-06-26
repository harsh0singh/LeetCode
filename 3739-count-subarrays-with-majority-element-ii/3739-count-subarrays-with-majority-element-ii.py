from typing import List
from bisect import bisect_left

class BIT:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    @property
    def n(self):
        return len(self.tree) - 1


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = [0]
        s = 0

        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            prefix.append(s)

        vals = sorted(set(prefix))
        bit = BIT(len(vals))

        ans = 0

        for p in prefix:
            idx = bisect_left(vals, p) + 1
            ans += bit.query(idx - 1)
            bit.update(idx, 1)

        return ans