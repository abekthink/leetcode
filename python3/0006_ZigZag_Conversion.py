#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""

        ln = len(s)
        if numRows == 1 or ln < numRows:
            return s

        output_chars = []
        step = (numRows - 1) * 2
        for row in range(numRows):
            if row == 0:
                first = 0
                while first < ln:
                    output_chars.append(s[first])
                    first += step
            else:
                first = 0
                while first < ln:
                    left_idx = first + row
                    if left_idx < ln:
                        output_chars.append(s[left_idx])
                    else:
                        break

                    right_idx = first + step - row
                    if right_idx < ln and right_idx != left_idx:
                        output_chars.append(s[right_idx])
                    first += step
        return ''.join(output_chars)


def main():
    s = Solution()
    print(s.convert("0123456789", 1))
    print(s.convert("0123456789", 2))
    print(s.convert("0123456789", 3))


if __name__ == '__main__':
    main()

