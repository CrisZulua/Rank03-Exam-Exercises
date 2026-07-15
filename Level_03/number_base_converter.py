#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   number_base_converter.py                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 10:04:31 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/14 11:41:50 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
#   Write a function that converts a number from one base to another.
#   Support bases from 2 to 36 inclusive.
#   Use digits 0-9 and letters A-Z for values 10-35.
#   Return "ERROR" for invalid inputs.
# Function signature
#   def number_base_converter(number: str, from_base: int, to_base: int) -> str:
# Examples
# Input
#   number_base_converter("1010", 2, 10)
# Output
#   "10"
# Input
#   number_base_converter("FF", 16, 10)
# Output
#   "255"
# Input
#   number_base_converter("255", 10, 16)
# Output
#   "FF"
# Input
#   number_base_converter("123", 10, 2)
# Output
#   "1111011"
# Input
#   number_base_converter("Z", 36, 10)
# Output
#   "35"
# Input
#   number_base_converter("35", 10, 36)
# Output
#   "Z"
# Input
#   number_base_converter("123", 1, 10)
# Output
#   "ERROR"
# Input
#   number_base_converter("G", 16, 10)
# Output
#   "ERROR"

def convert_to_int(number: str, from_base: int) -> str:
    num: str = ""
    return num


def convert_to_base(number: str, to_base: int) -> str:
    num = int(number, base=to_base)
    return str(num)


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if from_base < 2 or to_base < 2:
        return "ERROR"
    num: str = convert_to_int(number, from_base)
    res: str = convert_to_base(num, to_base)
    return res


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))  # Output: "10"
    print(number_base_converter("FF", 16, 10))   # Output: "255"
    print(number_base_converter("255", 10, 16))  # Output: "FF"
    print(number_base_converter("123", 10, 2))   # Output: "1111011"
    print(number_base_converter("Z", 36, 10))    # Output: "35"
    print(number_base_converter("35", 10, 36))   # Output: "Z"
    print(number_base_converter("123", 1, 10))   # Output: "ERROR"
    print(number_base_converter("G", 16, 10))     # Output: "ERROR"
