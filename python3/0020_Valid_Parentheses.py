#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    def isValid(self, s: str) -> bool:
        stack, bracket_mapping = [], {'{': '}', '[': ']', '(': ')'}
        for char in s:
            if char in bracket_mapping:
                stack.append(char)
            else:
                if not stack or char != bracket_mapping[stack.pop()]:
                    return False
        return not stack


def main():
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("]["))
    print(s.isValid("()]"))
    print(s.isValid("()["))


if __name__ == '__main__':
    main()
