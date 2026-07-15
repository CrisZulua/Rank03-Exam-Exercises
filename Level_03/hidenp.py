#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   hidenp.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/30 10:11:33 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 12:02:35 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# ----------
# Write a function that checks whether the string "small" is a subsequence
# of "big". All characters of "small" must appear in "big" in the same
# order, although not necessarily consecutively.
# The comparison is case-sensitive.
#
# Signature:
#   def hidenp(small: str, big: str) -> bool
#
# Examples:
#   Input:  hidenp("sing", "subsequence testing")
#   Output: True
#
#   Input:  hidenp("abc", "ab")
#   Output: False


def hidenp(small: str, big: str) -> bool:

    if len(small) > len(big):
        return False

    results: list[int] = []
    for c in small:
        results.append(big.find(c))

    if -1 in results:
        return False

    for i in range(len(results) - 1):
        if results[i] > results[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "bcde"))
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing", "subsequence testing"))
