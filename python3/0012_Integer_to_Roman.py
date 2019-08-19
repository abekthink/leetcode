#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_digits = [
            ['I', 'V', 'X'],
            ['X', 'L', 'C'],
            ['C', 'D', 'M'],
            ['M', '-', '-'],
        ]

        roman_str = ''
        digit_pos = 0
        while num > 0:
            digit = num % 10
            if digit == 0:
                temp_str = ''
            elif 0 < digit < 4:
                temp_str = roman_digits[digit_pos][0] * digit
            elif digit == 4:
                temp_str = roman_digits[digit_pos][0] + roman_digits[digit_pos][1]
            elif digit == 5:
                temp_str = roman_digits[digit_pos][1]
            elif 5 < digit < 9:
                temp_str = roman_digits[digit_pos][1] + roman_digits[digit_pos][0] * (digit - 5)
            else:
                temp_str = roman_digits[digit_pos][0] + roman_digits[digit_pos][2]

            roman_str = temp_str + roman_str
            num = num // 10
            digit_pos += 1
        return roman_str

    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_digits = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_str = ""
        for i, v in enumerate(values):
            roman_str += (num // v) * roman_digits[i]
            num %= v
        return roman_str


def main():
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))


if __name__ == '__main__':
    main()
