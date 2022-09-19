class Stack:
    stack = [5,12,19,17,2]
    history_of_max_elem = []
    max = 0

    def _push_elem_to_stack(self, object):
        object = int(object)
        self.stack = [object] + self.stack

        if object > self.max:
            self.max = object
            self.history_of_max_elem.append(object)

    def _pop_elem_from_stack(self):
        object = self.stack[0]; self.stack=self.stack[1:];

        if self.max == object:
            if self.history_of_max_elem:
                self.max = self.history_of_max_elem[-1]
            else:
                self.max = 0

    def command_handler(self, command):
        command = command.split()

        if command[0] == "push":
            self._push_elem_to_stack(command[-1])
        elif command[0] == "pop":
            self._pop_elem_from_stack()
        else:
            print(self.max)


stack = Stack()

stack.command_handler("pop")
stack.command_handler("push 7")
stack.command_handler("pop")
stack.command_handler("pop")
stack.command_handler("push 9")
stack.command_handler("push 12")
stack.command_handler("pop")
stack.command_handler("push 5")

print(stack.stack)