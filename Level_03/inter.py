#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   inter.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 09:51:23 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 12:02:36 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# ----------
# Write a function that returns a string containing the characters that appear
# in both strings, without repetitions.
# Characters are added in the order they first appear in the first string.
#
# Signature:
#   def inter(s1: str, s2: str) -> str
#
# Examples:
#   Input:  inter("hello", "world")
#   Output: "lo"
#
#   Input:  inter("banana", "band")
#   Output: "ban"


def inter(s1: str, s2: str) -> str:
    res: str = ""
    for char in s1:
        if char in s2:
            if char in res:
                continue
            res += char
    return res


if __name__ == "__main__":
    # 5 test cases
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))
