#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     if not s or len(s) <= 1:
    #         return s
    #     length = len(s)
    #     min_start = 0
    #     max_len = 1
    #     mid = 0
    #     while mid + max_len >> 1 < length:
    #         left = mid
    #         right = mid
    #         print("#", mid, left, right)
    #         while right < length - 1 and s[right] == s[right + 1]:
    #             right += 1
    #         print("##", mid, left, right)
    #         mid = right + 1
    #         print("###", mid, left, right)
    #         while right < length - 1 and left > 0 and s[right + 1] == s[left - 1]:
    #             right += 1
    #             left -= 1
    #         print("####", mid, left, right)
    #         if right - left + 1 > max_len:
    #             min_start = left
    #             max_len = right - left + 1
    #     return s[min_start: min_start + max_len]

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
        R: the next element to be examined (initially 0)
        C: the largest/left-most palindrome whose right boundary is R-1 (initially 0)
        i: the next palindrome to be calculated (initially 1)

        p[i]: palindrome radius in index-i position of T
        p[i] - 1: length of palindrome substring in s

        p[i] = R > i ? min(p[2 * C - i], R - i) : 1

        time complexity: O(n)

        related docs:
        https://www.cnblogs.com/grandyang/p/4475985.html
        https://blog.csdn.net/qxqxqzzz/article/details/84800939
        https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
        http://solutionleetcode.blogspot.com/2013/07/leetcode-longest-palindromic-substring.html
        http://en.wikipedia.org/wiki/Longest_palindromic_substring

        :param s: Given a string
        :return: The longest palindrome substring
        """
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        p = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            p[i] = (R > i) and min(R - i, p[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + p[i]] == T[i - 1 - p[i]]:
                p[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + p[i] > R:
                C, R = i, i + p[i]

        # Find the maximum element in P.
        max_len, center_index = max((n, i) for i, n in enumerate(p))
        return s[(center_index - max_len) >> 1: (center_index + max_len) >> 1]


def main():
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("abcbaa"))


if __name__ == '__main__':
    main()

