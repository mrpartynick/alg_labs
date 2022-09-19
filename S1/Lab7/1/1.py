
class SetWithArray:
    set_array = []
    in_f = open("input", "r")
    out_f = open("output", "w")

    ins_mode = "insertion"
    del_mode = "deleting"

    def __init__(self):
        line = self.in_f.readline()

        while (line):
            command = line[0]
            data = line[1:]
            if command == "A":
                self.add_data_in_set(data)
            elif command == "D":
                self.del_data_from_set(data)
            elif command == "?":
                self.is_data_in_set(data)
            print(self.set_array)
            line = self.in_f.readline()

        self.in_f.close()
        self.out_f.close()

    def add_data_in_set(self, data):
        if data not in self.set_array:
            index_of_insertion = self.find_needed_index(data, self.ins_mode)
            if index_of_insertion != None:
                self.set_array = self.set_array[:index_of_insertion] + [data] + self.set_array[index_of_insertion:]
            else:
                self.set_array.append(data)

    def del_data_from_set(self, data):
        del_index = self.find_needed_index(data, self.del_mode)
        self.set_array.pop(del_index)

    def is_data_in_set(self, data):
        if data in self.set_array:
            self.out_f.write("Y")
        else:
            self.out_f.write("N")
        self.out_f.write("\n")

    def find_needed_index(self, data, mode):
        index = 0
        for i in range(len(self.set_array)-2):
            if mode == "insertion":
                if self.set_array[i] < data and self.set_array[i+1] > data:
                    return index+1
                else:
                    index += 1
            elif mode == "deleting":
                if self.set_array[i] == data:
                    return index
                else:
                    index += 1


s = SetWithArray()