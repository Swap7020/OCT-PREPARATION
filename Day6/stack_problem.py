def is_valid(s):
    stack = []

    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


print(is_valid("{[()]}"))
print(is_valid("{[(])}"))
print(is_valid("((()))"))