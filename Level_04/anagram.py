#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   anagram.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 12:53:24 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/14 13:02:22 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
#   Write a function that checks if two strings are anagrams.
#   They must contain exactly the same letters with the same quantity,
#   ignoring case and spaces.
# Function signature
#   def anagram(s1: str, s2: str) -> bool:
# Examples
# Input
#   anagram("listen", "silent")
# Output
#   True
# Input
#   anagram("Triangle", "Integral")
# Output
#   True
# Input
#   anagram("Dormitory", "Dirty Room")
# Output
#   True
# Input
#   anagram("hello", "world")
# Output
#   False
# Input
#   anagram("", "")
# Output
#   True
# Input
#   anagram("abc", "abcc")
# Output
#   False

def anagram(s1: str, s2: str) -> bool:
    s1 = "".join(s1.split(' '))
    s2 = "".join(s2.split(' '))
    if len(s1) != len(s2):
        return False
    for c in s1.lower():
        if c not in s2.lower():
            return False
    return True


if __name__ == "__main__":
    print(anagram("listen", "silent"))        # Output: True
    print(anagram("Triangle", "Integral"))    # Output: True
    print(anagram("Dormitory", "Dirty Room"))  # Output: True
    print(anagram("hello", "world"))          # Output: False
    print(anagram("", ""))                    # Output: True
    print(anagram("abc", "abcc"))             # Output: False
