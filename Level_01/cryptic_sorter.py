# Assignment
# ----------
# Write a function that sorts a list of strings using multiple criteria:
# 1. Primary sort: by string length (shortest first)
# 2. Secondary sort: by ASCII order, ignoring case
# 3. Tertiary sort: by number of vowels (ascending)
# Equal strings keep their original input order.
#
# Example:
#   Input:  ["apple", "cat", "banana", "dog", "elephant"]
#   Output: ["cat", "dog", "apple", "banana", "elephant"]


def cryptic_sorter(strings: list[str]) -> list[str]:
    def vowels(string: str) -> int:
        string = string.lower()
        return (string.count('a') + string.count('e')
                + string.count('i') + string.count('o') + string.count('u'))

    strings.sort(key=lambda string: vowels(string))
    strings.sort(key=lambda string: string.lower())
    strings.sort(key=lambda string: len(string))
    return strings


listas: list[list[str]] = [["apple", "cat", "banana", "dog", "elephant"],
                           ["aaa", "bbb", "AAA", "BBB"],
                           ["hello", "world", "hi", "test"],
                           [""],
                           []]

if __name__ == "__main__":
    for lista in listas:
        print(cryptic_sorter(lista))
