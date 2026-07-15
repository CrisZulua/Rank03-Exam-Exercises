#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   string_sculptor.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/15 10:55:03 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 11:03:20 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# Write a function that transforms a string by alternating the case of
# alphabetic characters only.
# Non-alphabetic characters remain unchanged and are NOT counted in the
# alternation index.
# The first alphabetic character should be lowercase, the second uppercase, etc.
# Spaces reset the alternation (next alpha after a space is lowercase again).
# Function signature
# def string_sculptor(text: str) -> str:
# Examples
# Input
# string_sculptor("hello")
# Output
# "hElLo"
# Input
# string_sculptor("Hello World")
# Output
# "hElLo wOrLd"
# Input
# string_sculptor("abc123def")
# Output
# "aBc123DeF"
# Input
# string_sculptor("Python3.9!")
# Output
# "pYtHoN3.9!"
# Input
# string_sculptor("")
# Output
# ""

def string_sculptor(text: str) -> str:
    alt = 0
    res = ""
    for c in text:
        if c == ' ':
            alt = 0
            res += ' '
            continue
        if c.isalpha():
            if alt == 0:
                res += c.lower()
                alt = 1
            elif alt == 1:
                alt = 0
                res += c.upper()
        else:
            res += c
    return res


if __name__ == "__main__":
    print(string_sculptor("hello"))  # Output: "hElLo"
    print(string_sculptor("Hello World"))  # Output: "hElLo wOrLd"
    print(string_sculptor("abc123def"))  # Output: "aBc123DeF"
    print(string_sculptor("Python3.9!"))  # Output: "pYtHoN3.9!"
    print(string_sculptor(""))  # Output: ""
