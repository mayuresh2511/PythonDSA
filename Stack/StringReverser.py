from Stack import Stack


def reverse_string(stack, input_str):
    for letter in input_str:
        stack.push(letter)
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


stack_obj = Stack()
print(reverse_string(stack_obj, "!evitacudE ot emocleW"))

