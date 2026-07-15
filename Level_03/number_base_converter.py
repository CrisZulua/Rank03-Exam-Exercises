#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   number_base_converter.py                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 10:04:31 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 12:29:55 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# ----------
# Write a function that converts a number from one base to another.
# Support bases from 2 to 36 inclusive, using digits 0-9 and letters A-Z.
# Return "ERROR" for invalid inputs.
#
# Signature:
#   def number_base_converter(number: str, from_base: int, to_base: int) -> str
#
# Examples:
#   Input:  number_base_converter("1010", 2, 10)
#   Output: "10"
#
#   Input:  number_base_converter("FF", 16, 10)
#   Output: "255"
#
#   Input:  number_base_converter("123", 1, 10)
#   Output: "ERROR"


def convert_to_int(number: str, from_base: int) -> int:
    if not (2 <= from_base <= 36):
        raise ValueError("Invalid base")
    if not number:
        raise ValueError("Empty number")

    return int(number, from_base)


def convert_to_base(number: int, to_base: int) -> str:
    if not (2 <= to_base <= 36):
        raise ValueError("Invalid base")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_number = ""

    while number > 0:
        new_number += digits[number % to_base]
        number = number // to_base

    return new_number[::-1]


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    try:
        decimal_value = convert_to_int(number, from_base)
        return convert_to_base(decimal_value, to_base)
    except ValueError:
        return "ERROR"


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))  # Output: "10"
    print(number_base_converter("FF", 16, 10))   # Output: "255"
    print(number_base_converter("255", 10, 16))  # Output: "FF"
    print(number_base_converter("123", 10, 2))   # Output: "1111011"
    print(number_base_converter("Z", 36, 10))    # Output: "35"
    print(number_base_converter("35", 10, 36))   # Output: "Z"
    print(number_base_converter("123", 1, 10))   # Output: "ERROR"
    print(number_base_converter("G", 16, 10))     # Output: "ERROR"
