#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   twist_sequence.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/15 11:05:27 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 11:14:52 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# Write a function that rotates an array to the right by k positions.
# Rotating right by k means the last k elements move to the front.
# Function signature
# def twist_sequence(arr: list[int], k: int) -> list[int]:
# Examples
# Input
# twist_sequence([1,2,3,4,5], 2)
# Output
# [4,5,1,2,3]
# Input
# twist_sequence([1,2,3], 1)
# Output
# [3,1,2]
# Input
# twist_sequence([1,2,3,4], 0)
# Output
# [1,2,3,4]
# Input
# twist_sequence([1,2,3], 5)
# Output
# [2,3,1]
# Input
# twist_sequence([], 3)
# Output
# []

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    return arr[-k % len(arr):] + arr[:-k % len(arr)]


if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    print(twist_sequence([1, 2, 3], 1))
    print(twist_sequence([1, 2, 3, 4], 0))
    print(twist_sequence([1, 2, 3], 5))
    print(twist_sequence([], 3))
