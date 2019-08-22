#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            while i < len(nums) - 1 and nums[i] != val:
                i += 1
            while j > 0 and nums[j] == val:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
        return i if nums[i] == val else i + 1


def main():
    s = Solution()
    nums = [3, 2, 2, 3]
    print(s.removeElement(nums, 3), nums)
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(s.removeElement(nums, 2), nums)
    nums = [2, 3, 2]
    print(s.removeElement(nums, 2), nums)
    nums = [2, 2, 2]
    print(s.removeElement(nums, 2), nums)
    nums = [2, 2, 2]
    print(s.removeElement(nums, 3), nums)
    nums = [1]
    print(s.removeElement(nums, 1), nums)


if __name__ == '__main__':
    main()
