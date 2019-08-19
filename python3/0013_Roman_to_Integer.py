#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    def romanToInt(self, s: str) -> int:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_digits = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        res = 0
        while s:
            while s.startswith(roman_digits[index]):
                res += values[index]
                s = s[len(roman_digits[index]):]
            index += 1
        return res


def main():
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('IV'))
    print(s.romanToInt('IX'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))


if __name__ == '__main__':
    main()
