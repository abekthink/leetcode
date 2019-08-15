#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     if nums is None or len(nums) < 2:
    #         return []
    #     ln = len(nums)
    #     for i in range(0, ln - 1):
    #         for j in range(i + 1, ln):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     if nums is None or len(nums) < 2:
    #         return []
    #     for index, num in enumerate(nums):
    #         diff = target - num
    #         if diff in nums[index + 1:]:
    #             idx = nums[index + 1:].index(diff)
    #             return [index, index + 1 + idx]

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     if nums is None:
    #         return []
    #     num_dict = dict()
    #     for index, num in enumerate(nums):
    #         diff = target - num
    #         if diff in num_dict:
    #             return [num_dict[diff], index]
    #         num_dict[num] = index
    #     return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return []
        sorted_nums = [(val, index) for index, val in enumerate(nums)]
        sorted_nums.sort()
        begin, end = 0, len(sorted_nums) - 1
        while begin < end:
            sum = sorted_nums[begin][0] + sorted_nums[end][0]
            if sum == target:
                return [sorted_nums[begin][1], sorted_nums[end][1]]
            elif sum > target:
                end -= 1
            else:
                begin += 1
        return []


def main():
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    main()
