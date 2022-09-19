class Queue:
    queue = []

    def command_handler(self, command):
        if command[0] == "+":
            self.queue = [int(command[1:])] + self.queue
        elif command == "-":
            self.queue = self.queue[:-1]
        else:
            print("Invalid command ")

q = Queue()

q.command_handler("+ 10")
q.command_handler("+ 20")

print(q.queue)

q.command_handler("-")

print(q.queue)

