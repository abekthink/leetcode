#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List, bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = bisect.bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target, lo=left + 1)
        return [left, right - 1]


def main():
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(s.searchRange([], 6))
    print(s.searchRange([2, 2], 3))


if __name__ == '__main__':
    main()
