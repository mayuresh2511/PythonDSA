from Stack import Stack


def is_match(top, paren):

    if top == "[" and paren == "]":
        return True
    elif top == "(" and paren == ")":
        return True
    elif top == "{" and paren == "}":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    stack = Stack()

    for paren in paren_string:

        if paren in "([{":
            stack.push(paren)
        else:
            if stack.is_empty():
                return False
            else:
                top = stack.pop()
                if not is_match(top, paren):
                    return False

    if stack.is_empty():
        return True
    else:
        return False


if __name__ == "main":
    print(is_paren_balanced("(){}("))
