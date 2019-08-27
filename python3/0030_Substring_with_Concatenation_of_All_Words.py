#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List


class Solution:
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     if len(words) == 0 or len(s) == 0 or len(s) < len(''.join(words)):
    #         return []
    #     word_len, word_count = len(words[0]), len(words)
    #     word_sorted_comb = ''.join(sorted(words))
    #     word_all_len = len(word_sorted_comb)
    #     res = []
    #     for i in range(len(s) - word_all_len + 1):
    #         word_seq = [s[i + j * word_len: i + (j + 1) * word_len] for j in range(word_count)]
    #         word_comb = ''.join(sorted(word_seq))
    #         if word_comb == word_sorted_comb:
    #             res.append(i)
    #     return res

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(s) == 0 or len(s) < len(''.join(words)):
            return []

        str_len, word_len = len(s), len(words[0])
        substr_len = len(words) * word_len
        times = {}
        for word in words:
            if word in times:
                times[word] += 1
            else:
                times[word] = 1

        res = []

        def findAnswer(str_start):
            word_start = str_start
            cur = {}
            while str_start + substr_len <= str_len:
                word = s[word_start:word_start + word_len]
                word_start += word_len
                if word not in times:
                    str_start = word_start
                    cur.clear()
                else:
                    if word in cur:
                        cur[word] += 1
                    else:
                        cur[word] = 1
                    while cur[word] > times[word]:
                        cur[s[str_start:str_start + word_len]] -= 1
                        str_start += word_len
                    if word_start - str_start == substr_len:
                        res.append(str_start)

        for i in range(min(word_len, str_len - substr_len + 1)):
            findAnswer(i)
        return res


def main():
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))


if __name__ == '__main__':
    main()
