#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     index = 0
    #     while index < len(nums):
    #         while index + 1 < len(nums) and nums[index] == nums[index + 1]:
    #             nums.pop(index + 1)
    #         index += 1
    #     return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i + 1


def main():
    s = Solution()
    nums = [1, 1, 2]
    print(s.removeDuplicates(nums), nums)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(nums), nums)
    nums = [1, 2]
    print(s.removeDuplicates(nums), nums)


if __name__ == '__main__':
    main()
