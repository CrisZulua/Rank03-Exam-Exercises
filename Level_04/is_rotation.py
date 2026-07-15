#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   is_rotation.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/15 10:21:12 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 12:02:40 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# ----------
# Write a function that determines whether the second list is a rotation of
# the first list (left or right).
# A rotation means that the elements are shifted circularly.
# If the arrays have different lengths, they cannot be rotations of each other.
# Two empty arrays are considered rotations of each other.
#
# Signature:
#   def is_rotation(arr1: list, arr2: list) -> bool
#
# Examples:
#   Input:  is_rotation([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])
#   Output: True
#
#   Input:  is_rotation([1, 2, 3], [3, 2, 1])
#   Output: False

from typing import Any


def is_rotation(arr1: list[Any], arr2: list[Any]) -> bool:
    if len(arr1) != len(arr2):
        return False
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    try:
        fe_pos = arr2.index(arr1[0])
    except ValueError:
        return False
    ordered_array = arr2[fe_pos:] + arr2[:fe_pos]
    if ordered_array != arr1:
        return False
    return True


if __name__ == "__main__":
    print(is_rotation([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))  # Output: True
    print(is_rotation([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))  # Output: True
    print(is_rotation([1, 2, 3], [3, 2, 1]))              # Output: False
    print(is_rotation([1, 2], [1, 2, 3]))                 # Output: False
    print(is_rotation([], []))                            # Output: True
