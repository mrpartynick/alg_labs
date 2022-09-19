class Stack:
    value_of_elements = 0
    head = None
    # Функции добавления элемента
    def push(self, data):
        elem_for_adding = Elem_Of_Stack(data)
        elem_for_adding.next_elem = self.head
        self.head = elem_for_adding
        self.value_of_elements += 1

    def pop(self):
        self.head = self.head.next_elem

    def isEmpty(self):
        if self.value_of_elements == 0:
            return True
        else:
            return False

    def print_stack(self):
        s = ""
        element = self.head
        while (element):
            s += str(element.data) + " "
            element = element.next_elem
        print(s)


class Elem_Of_Stack:

    def __init__(self, data):
        self.data = data
        self.next_elem = None


stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(1)
stack.push(13)
stack.pop()
stack.push(84)
stack.push(18)
stack.push(99)
stack.push(101)
stack.pop()
print(stack.isEmpty())

stack.print_stack()
