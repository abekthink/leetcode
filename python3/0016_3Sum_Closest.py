#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(n^2)
        nums.sort()
        min_distance, closest_sum = None, None
        ln = len(nums)
        for i in range(ln - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            low, high = i + 1, ln - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                distance = s - target

                if min_distance is None or abs(distance) < min_distance:
                    min_distance = abs(distance)
                    closest_sum = s
                    if distance > 0:
                        high -= 1
                    else:
                        low += 1
                    while 1 < low < high and nums[low - 1] == nums[low]:
                        low += 1
                    while low < high < ln - 1 and nums[high] == nums[high + 1]:
                        high -= 1
                elif distance > 0:
                    high -= 1
                else:
                    low += 1
        return closest_sum


def main():
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([0, 2, 1, -3], 1))
    print(s.threeSumClosest([1, 1, -1, -1, 3], -1))
    print(s.threeSumClosest(
        [13, 2, 0, -14, -20, 19, 8, -5, -13, -3, 20, 15, 20, 5, 13, 14, -17, -7, 12, -6, 0, 20, -19, -1, -15, -2, 8, -2,
         -9, 13, 0, -3, -18, -9, -9, -19, 17, -14, -19, -4, -16, 2, 0, 9, 5, -7, -4, 20, 18, 9, 0, 12, -1, 10, -17, -11,
         16, -13, -14, -3, 0, 2, -18, 2, 8, 20, -15, 3, -13, -12, -2, -19, 11, 11, -10, 1, 1, -10, -2, 12, 0, 17, -19,
         -7, 8, -19, -17, 5, -5, -10, 8, 0, -12, 4, 19, 2, 0, 12, 14, -9, 15, 7, 0, -16, -5, 16, -12, 0, 2, -16, 14, 18,
         12, 13, 5, 0, 5, 6], -59))


if __name__ == '__main__':
    main()
