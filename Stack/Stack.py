
class Stack:

    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items


if __name__ == "main":

    stack_obj = Stack()

    stack_obj.push(4)
    stack_obj.push(3)
    stack_obj.push(2)
    stack_obj.push(1)

    print(stack_obj.pop())
    print(stack_obj.get_stack())


