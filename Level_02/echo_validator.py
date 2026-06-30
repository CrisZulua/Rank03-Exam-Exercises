# Write a function that checks if a string is a palindrome,
# ignoring spaces and case, only consider alphabetic characters
# for the comparison.

def echo_validator(text: str) -> bool:
    if text == "":
        return False
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        return True
    return False


test_cases = [
    # True cases (Palindromes)
    ("a", True),
    ("aa", True),
    ("aba", True),
    ("abba", True),
    ("racecar", True),
    ("level", True),
    ("noon", True),
    ("madam", True),
    ("kayak", True),
    ("civic", True),
    ("radar", True),
    ("A man a plan a canal Panama", True),
    ("Race car", True),
    ("Madam Im Adam", True),
    ("Was it a car or a cat I saw", True),
    ("Never odd or even", True),
    ("A Santa at NASA", True),
    ("12321", True),  # Only alphabetic, so becomes empty
    ("", True),
    ("a", True),
    # False cases (Non-palindromes)
    ("ab", False),
    ("abc", False),
    ("hello", False),
    ("python", False),
    ("racecar2extra", False),
    ("Aba B", False),
    ("abcd", False),
    ("test", False),
    ("code", False),
    ("12345", False),
    ("aab", False),
    ("xyz", False),
    ("Hello World", False),
    ("The quick brown fox", False),
    ("almost", False),
]

if __name__ == "__main__":
    text = "hola"
    print(text[::-1])
    for test in test_cases:
        print(test[0], echo_validator(test[0]) == test[1])
