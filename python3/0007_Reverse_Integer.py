#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from math import pow

MAX_INT = int(pow(2, 31)) - 1
MIN_INT = -int(pow(2, 31))


class Solution:
    # def reverse(self, x: int) -> int:
    #     max_int = 2 ** 31 - 1
    #     min_int = -2 ** 31
    #
    #     if x == 0:
    #         return 0
    #
    #     negative = False
    #     if x < 0:
    #         x = -x
    #         negative = True
    #
    #     digits = []
    #     while x > 0:
    #         remainder = x % 10
    #         x = x // 10
    #         digits.append(remainder)
    #     nonzero_idx = 0
    #     while digits[nonzero_idx] == 0:
    #         nonzero_idx += 1
    #     res = ''.join(map(str, digits[nonzero_idx:]))
    #     res = int(res)
    #     if negative:
    #         res = -res
    #     if res > max_int or res < min_int:
    #         return 0
    #     return res

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        negative = False
        if x < 0:
            x = -x
            negative = True

        reversed_num = 0
        while x > 0:
            remainder = x % 10
            x = x // 10
            reversed_num = reversed_num * 10 + remainder

        if negative:
            reversed_num = -reversed_num

        if reversed_num > MAX_INT or reversed_num < MIN_INT:
            return 0
        return reversed_num


def main():
    s = Solution()
    print(s.reverse(0))
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(-120))
    print(s.reverse(2 ** 31))
    print(s.reverse(2 ** 31 - 1))
    print(s.reverse(-1 * 2 ** 31))
    print(s.reverse(-1 * 2 ** 31 - 1))


if __name__ == '__main__':
    main()
