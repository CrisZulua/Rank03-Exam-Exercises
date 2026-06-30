# Write a function that sorts a list of strings according to multiple criteria:
# 1. Primary sort: By string length (shortest first)
# 2. Secondary sort: ASCII order, except letters are compared
# case-insensitively
#    (for strings of same length)
# 3. Tertiary sort: By number of vowels (ascending, for same length and
# 4. Equal strings will appear in the same order as in the input list.

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
