# Write a function that checks if the brackets in a string are valid.
# A string is valid if every opening bracket has a matching closing bracket
# in the correct order.
# Allowed brackets: (), [], {}

def bracket_validator(s: str) -> bool:
    stack: list[str] = []
    pairs: dict[str, str] = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in ('(', '{', '['):
            stack.append(c)
        elif c in (')', '}', ']'):
            if not stack.pop() is pairs[c]:
                return False
        else:
            return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    print(bracket_validator("(({[]}))[]{}()"))
