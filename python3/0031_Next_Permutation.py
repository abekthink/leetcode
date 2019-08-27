#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = i + 1
                while j < length and nums[j] > nums[i - 1]:
                    j += 1
                nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
                nums[i:] = nums[length - 1:i - 1:-1]
                return
        nums.reverse()


def main():
    s = Solution()
    nums = [1, 2, 3]
    print(s.nextPermutation(nums), nums)
    nums = [3, 2, 1]
    print(s.nextPermutation(nums), nums)
    nums = [1, 1, 5]
    print(s.nextPermutation(nums), nums)
    nums = [1, 3, 2]
    print(s.nextPermutation(nums), nums)


if __name__ == '__main__':
    main()
