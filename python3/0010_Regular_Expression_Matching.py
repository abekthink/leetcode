#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    #     import re
    #     return re.match('^' + p + '$', s) is not None

    # def isMatch(self, s: str, p: str) -> bool:
    #     """
    #     Recursive algorithm
    #
    #     :param s: Given a string
    #     :param p: Given a pattern
    #     :return: whether this pattern matches the given string
    #     """
    #     if not p:
    #         return True if not s else False
    #     if len(p) == 1:
    #         return True if len(s) == 1 and (p == '.' or p == s) else False
    #     if p[1] != '*':
    #         return s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
    #     return self.isMatch(s, p[2:]) or (s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))

    def isMatch(self, s: str, p: str) -> bool:
        """
        Dynamic programming

        dp[i][j]: means first j letters of p can match first i letters of s

        :param s: Given a string
        :param p: Given a pattern
        :return: whether this pattern matches the given string
        """
        lens, lenp = len(s), len(p)
        dp = [[False] * (lenp + 1) for _ in range(lens + 1)]

        dp[0][0] = True
        for j in range(2, lenp + 1, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in range(1, lens + 1):
            for j in range(1, lenp + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (p[j - 2] in {s[i - 1], '.'} and dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in {'.', s[i - 1]}

        return dp[lens][lenp]


def main():
    s = Solution()
    print(s.isMatch("aa", "a"))
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("ab", ".*"))
    print(s.isMatch("aab", "c*a*b"))


if __name__ == '__main__':
    main()

