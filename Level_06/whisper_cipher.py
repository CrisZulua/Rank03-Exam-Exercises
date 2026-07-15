#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   whisper_cipher.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: czuluaga <czuluaga@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/15 11:27:42 by czuluaga            #+#    #+#            #
#   Updated: 2026/07/15 11:57:11 by czuluaga           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Assignment
# Write a function that creates a Caesar cipher by shifting letters in a
# string by a given amount.
# Non-alphabetic characters should remain unchanged.
# The shift can be negative (shift left).
# Function signature
# def whisper_cipher(text: str, shift: int) -> str:
# Examples
# Input
# whisper_cipher("hello", 3)
# Output
# "khoor"
# Input
# whisper_cipher("Hello World!", 1)
# Output
# "Ifmmp Xpsme!"
# Input
# whisper_cipher("xyz", 3)
# Output
# "abc"
# Input
# whisper_cipher("ABC123def", 5)
# Output
# "FGH123ijk"
# Input
# whisper_cipher("", 10)
# Output
# ""
# Input
# whisper_cipher("abc", -3)
# Output
# "xyz"

def whisper_cipher(text: str, shift: int) -> str:
    res = ""
    for c in text:
        if c.isalpha():
            value = ord(c)
            if c.isupper():
                value = ((value - 65 + shift) % 26) + 65
            else:
                value = ((value - 97 + shift) % 26) + 97
            res += chr(value)
        else:
            res += c
    return res


if __name__ == "__main__":
    # Test cases
    print(whisper_cipher("hello", 3))  # Output: "khoor"
    print(whisper_cipher("Hello World!", 1))  # Output: "Ifmmp Xpsme!"
    print(whisper_cipher("xyz", 3))  # Output: "abc"
    print(whisper_cipher("ABC123def", 5))  # Output: "FGH123ijk"
    print(whisper_cipher("", 10))  # Output: ""
    print(whisper_cipher("abc", -3))  # Output: "xyz"
