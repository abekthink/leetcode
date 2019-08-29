#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     def search_num(low: int, high: int) -> int:
    #         if low > high:
    #             return -1
    #         mid = (low + high) // 2
    #         if nums[mid] == target:
    #             return mid
    #         if nums[low] <= target < nums[mid] or target < nums[mid] < nums[high] or nums[mid] < nums[high] < target:
    #             return search_num(low, mid - 1)
    #         else:
    #             return search_num(mid + 1, high)
    #
    #     return search_num(0, len(nums) - 1)

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= target < nums[mid] or target < nums[mid] < nums[high] or nums[mid] < nums[high] < target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


def main():
    s = Solution()
    print(s.search([1, 3], 3))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(s.search([1, 3, 5], 3))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 5))


if __name__ == '__main__':
    main()
