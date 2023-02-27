from Stack import Stack


def int_to_bin_converter(stack, number):

    while number > 0:

        stack.push(number % 2)
        number = number // 2

    bin_number = ""
    while not stack.is_empty():
        bin_number += str(stack.pop())

    return bin_number


stack_obj = Stack()

print(int_to_bin_converter(stack_obj, 56))
