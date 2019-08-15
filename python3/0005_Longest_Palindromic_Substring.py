#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     """
    #     dynamic programming:
    #
    #     dp[i][j]: boolean, represent s[i: j+1] whether is palindrome
    #
    #                 | True,                                 i == j
    #     dp[i][j] =  | s[i] == s[j],                         i - j == 1
    #                 | s[i] == s[j] && dp[i + 1][j + 1],     i - j > 1
    #
    #     time complexity: O(n^2)
    #     space complexity: O(n^2)
    #
    #     :param s: Given a string
    #     :return: The longest palindrome substring
    #     """
    #     ln = len(s)
    #     dp = [[False for _ in range(ln)] for _ in range(ln)]
    #
    #     max_str = ''
    #     for step in range(ln):
    #         for i in range(ln - step):
    #             j = i + step
    #             if step == 0:
    #                 dp[i][j] = True
    #             elif step == 1:
    #                 dp[i][j] = True if s[i] == s[j] else False
    #             else:
    #                 dp[i][j] = True if s[i] == s[j] and dp[i + 1][j - 1] is True else False
    #
    #             if dp[i][j] is True and step + 1 > len(max_str):
    #                 max_str = s[i: j+1]
    #     return max_str

    def longestPalindrome(self, s: str) -> str:
        """
        Manacher's Algorithm:
        s -> T: abc -> ^#a#b#c#$
        idx: center of the palindrome substring
        mx: right side of the palindrome substring
        p[i]: palindrome radius in index-i position of T
        p[i] - 1: length of palindrome substring in s

        p[i] = mx > i ? min(p[2 * idx - i], mx - i) : 1

        time complexity: O(n)

        related docs:
        https://www.cnblogs.com/grandyang/p/4475985.html
        https://blog.csdn.net/qxqxqzzz/article/details/84800939
        https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
        http://en.wikipedia.org/wiki/Longest_palindromic_substring

        :param s: Given a string
        :return: The longest palindrome substring
        """
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        p = [0] * n
        idx = mx = 0
        for i in range(1, n - 1):
            p[i] = (mx > i) and min(mx - i, p[2 * idx - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + p[i]] == T[i - 1 - p[i]]:
                p[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + p[i] > mx:
                idx, mx = i, i + p[i]

        # Find the maximum element in P.
        max_len, center_index = max((n, i) for i, n in enumerate(p))
        return s[(center_index - max_len) >> 1: (center_index + max_len) >> 1]


def main():
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))


if __name__ == '__main__':
    main()

