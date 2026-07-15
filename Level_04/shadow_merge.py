#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   shadow_merge.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/15 10:33:06 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 10:35:40 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# Write a function that merges two sorted lists into one sorted list.
# Function signature
# def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
# Examples
# Input
# shadow_merge([1,3,5], [2,4,6])
# Output
# [1,2,3,4,5,6]
# Input
# shadow_merge([1,2,3], [4,5,6])
# Output
# [1,2,3,4,5,6]
# Input
# shadow_merge([1], [2,3,4])
# Output
# [1,2,3,4]
# Input
# shadow_merge([], [1,2,3])
# Output
# [1,2,3]
# Input
# shadow_merge([1,1,2], [1,3,3])
# Output
# [1,1,1,2,3,3]

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)


if __name__ == "__main__":
    print(shadow_merge([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
    print(shadow_merge([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
    print(shadow_merge([1], [2, 3, 4]))        # Output: [1, 2, 3, 4]
    print(shadow_merge([], [1, 2, 3]))         # Output: [1, 2, 3]
    print(shadow_merge([1, 1, 2], [1, 3, 3]))   # Output: [1, 1, 1, 2, 3, 3]
