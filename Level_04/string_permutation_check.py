#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   string_permutation_check.py                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/15 10:36:43 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 10:43:54 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# Write a function that determines if two strings are permutations of each other.
# Case sensitive. Whitespace and punctuation count as regular characters.
# Empty strings are permutations of each other.
# Function signature
# def string_permutation_checker(s1: str, s2: str) -> bool:
# Examples
# Input
# string_permutation_checker("abc", "bca")
# Output
# True
# Input
# string_permutation_checker("abc", "def")
# Output
# False
# Input
# string_permutation_checker("listen", "silent")
# Output
# True
# Input
# string_permutation_checker("hello", "bello")
# Output
# False
# Input
# string_permutation_checker("", "")
# Output
# True
# Input
# string_permutation_checker("a", "")
# Output
# False
# Input
# string_permutation_checker("Abc", "abc")
# Output
# False
# Input
# string_permutation_checker("a gentleman","elegant man")
# Output
# True

def string_permutation_checker(s1: str, s2: str) -> bool:
    if s1 == "" and s2 == "":
        return True
    if len(s1) != len(s2):
        return False
    s1_dict = {}
    s2_dict = {}
    for c in s1:
        s1_dict[c] = s1.count(c)
    for c in s2:
        s2_dict[c] = s2.count(c)
    if s1_dict != s2_dict:
        return False
    return True


if __name__ == "__main__":
    print(string_permutation_checker("abc", "bca"))  # True
    print(string_permutation_checker("abc", "def"))  # False
    print(string_permutation_checker("listen", "silent"))  # True
    print(string_permutation_checker("hello", "heloo"))  # False
    print(string_permutation_checker("", ""))  # True
    print(string_permutation_checker("a", ""))  # False
    print(string_permutation_checker("Abc", "abc"))  # False
    print(string_permutation_checker("a gentleman", "elegant man"))  # True
