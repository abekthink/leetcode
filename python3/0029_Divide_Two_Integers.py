#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

MAX_INT = (1 << 31) - 1
MIN_INT = -(1 << 31)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        minus = dividend < 0 < divisor or dividend > 0 > divisor
        dividend, divisor, count = abs(dividend), abs(divisor), 0
        origin_divisor = divisor
        while divisor <= dividend:
            divisor <<= 1
            count += 1
        divisor >>= 1
        count -= 1

        quotient = 0
        while dividend >= origin_divisor:
            dividend -= divisor
            quotient += 1 << count

            while origin_divisor <= dividend < divisor:
                divisor >>= 1
                count -= 1
        if minus:
            quotient = -quotient
        return MAX_INT if quotient > MAX_INT or quotient < MIN_INT else quotient


def main():
    s = Solution()
    print(s.divide(10, 3))
    print(s.divide(7, -3))
    print(s.divide(-2147483648, -1))


if __name__ == '__main__':
    main()
