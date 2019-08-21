#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List, bisect


class Solution:
    # merge sort
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     m, n = len(nums1), len(nums2)
    #     i = j = 0
    #     nums3 = list()
    #     while i < m and j < n:
    #         if nums1[i] < nums2[j]:
    #             nums3.append(nums1[i])
    #             i += 1
    #         else:
    #             nums3.append(nums2[j])
    #             j += 1
    #
    #     if i < m:
    #         nums3.extend(nums1[i:])
    #     if j < n:
    #         nums3.extend(nums2[j:])
    #
    #     mid = (m + n) // 2
    #     if (m + n) % 2 == 0:
    #         return (nums3[mid - 1] + nums3[mid]) / 2
    #     else:
    #         return nums3[mid]

    # binary search: self-made
    # def findMedianSortedArrays(self, nums1, nums2):
    #     nums1, nums2 = sorted((nums1, nums2), key=len)
    #     m, n = len(nums1), len(nums2)
    #     mid = (m + n - 1) >> 1
    #     low, high = 0, m
    #     while low < high:
    #         i = (low + high) >> 1
    #         if mid - i - 1 < 0 or nums1[i] >= nums2[mid - i - 1]:
    #             high = i
    #         else:
    #             low = i + 1
    #     mid_idx = low
    #     mid_nums = sorted(nums1[mid_idx:mid_idx + 2] + nums2[mid - mid_idx:mid - mid_idx + 2])
    #     return (mid_nums[0] + mid_nums[1 - (m + n) % 2]) / 2.0

    # binary search: bisect.bisect_left
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = sorted((nums1, nums2), key=len)
        m, n = len(nums1), len(nums2)
        mid = (m + n - 1) >> 1

        class Range:
            def __getitem__(self, idx):
                return mid - idx - 1 < 0 or nums1[idx] >= nums2[mid - idx - 1]

        mid_idx = bisect.bisect_left(Range(), True, 0, m)
        mid_nums = sorted(nums1[mid_idx:mid_idx + 2] + nums2[mid - mid_idx:mid - mid_idx + 2])
        return (mid_nums[0] + mid_nums[1 - (m + n) % 2]) / 2.0


def main():
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 2], [3, 4]))


if __name__ == '__main__':
    main()
