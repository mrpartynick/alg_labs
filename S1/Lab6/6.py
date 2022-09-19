class QueueWithPriority:
    queue = []
    input_file = open("input.txt.txt", "r")
    output_file = open("output.txt", "w")

    def __init__(self):
        number_of_line = 0
        lines = self.input_file.readlines()
        for line in lines:
            number_of_line += 1
            self.command_handler(line, number_of_line)

    def command_handler(self, command, number_of_line):
        command = command.split()
        if command[0] == "A":
            self.insert_min(int(command[1:]), number_of_line)
        elif command[0] == "D":
            if self.queue:
                self.output_file.write(str(self.queue.pop(0)))
            else:
                self.output_file.write("*")
            self.output_file.write("/n")
        else:
            self.change_value_in_line(command[1], command[2])



    def insert_min(self, elem_for_adding, number_of_line):
        index_of_insertion = 0
        for elements in self.queue:
            if elem_for_adding < elements:
                break
            else:
                index_of_insertion += 1
        self.queue = self.queue[:index_of_insertion] + [[elem_for_adding,number_of_line]] + self.queue[index_of_insertion:]

    def change_value_in_line(self, num_of_line, value):
        index_of_element = 0
        for elem in self.queue:
            if elem[1] == num_of_line:
                elem_for_insertion = elem
                self.queue.pop(index_of_element)
                break
            else:
                index_of_element += 1

        self.insert_min(value, num_of_line)


