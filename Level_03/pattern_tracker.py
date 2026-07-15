#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   pattern_tracker.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 12:39:43 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/14 12:52:06 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
#   Write a function that counts the number of valid consecutive digit pairs
#   in a string. A valid pair consists of two adjacent digits where the second
#   digit is exactly one greater than the first.
#   A 9 followed by a 0 is NOT a valid pair.
# Function signature
#   def pattern_tracker(text: str) -> int:
# Examples
# Input
#   pattern_tracker("123")
# Output
#   2
# Input
#   pattern_tracker("12a34")
# Output
#   2
# Input
#   pattern_tracker("987654321")
# Output
#   0
# Input
#   pattern_tracker("01234567")
# Output
#   7
# Input
#   pattern_tracker("abc")
# Output
#   0
# Input
#   pattern_tracker("1a2b3c4")
# Output
#   0
# Input
#   pattern_tracker("112233")
# Output
#   2

def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i]) == int(text[i + 1]) - 1:
                count += 1
    return count


if __name__ == "__main__":
    # Test cases
    print(pattern_tracker("123"))          # Output: 2
    print(pattern_tracker("12a34"))        # Output: 2
    print(pattern_tracker("987654321"))    # Output: 0
    print(pattern_tracker("01234567"))     # Output: 7
    print(pattern_tracker("abc"))          # Output: 0
    print(pattern_tracker("1a2b3c4"))      # Output: 0
    print(pattern_tracker("112233"))       # Output: 2
