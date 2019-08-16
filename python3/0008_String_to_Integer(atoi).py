#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

import re

MAX_INT = 2 ** 31 - 1
MIN_INT = -2 ** 31


class Solution:
    # def myAtoi(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     idx = 0
    #     while idx < len(s) and s[idx] == ' ':
    #         idx += 1
    #     if not s[idx:]:
    #         return 0
    #
    #     valid_sign = {'+', '-'}
    #     valid_digits = set([str(i) for i in range(10)])
    #
    #     sign = None
    #     if s[idx] in valid_sign:
    #         sign = s[idx]
    #         idx += 1
    #     elif s[idx] not in valid_digits:
    #         return 0
    #
    #     num = 0
    #     ln = len(s)
    #     while idx < ln and s[idx] in valid_digits:
    #         num = num * 10 + int(s[idx])
    #         idx += 1
    #
    #     if sign == '-':
    #         num = -num
    #
    #     if num > MAX_INT:
    #         return MAX_INT
    #     elif num < MIN_INT:
    #         return MIN_INT
    #     return num

    def myAtoi(self, s: str) -> int:
        p = re.compile(r'^\s*([+\-]?\d+)')
        m = p.match(s)
        if m is None:
            return 0

        num = int(m.group(0))
        if num > MAX_INT:
            return MAX_INT
        elif num < MIN_INT:
            return MIN_INT
        return num


def main():
    s = Solution()
    print(s.myAtoi(""))
    print(s.myAtoi(" "))
    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("+987 words and"))
    print(s.myAtoi("3.14159"))


if __name__ == '__main__':
    main()
