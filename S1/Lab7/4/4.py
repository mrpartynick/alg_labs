class Dictionary:
    in_f = open("input", "r")
    out_f = open("output", "w")

    dictionary = {}
    out_arr = []
    previous = ""

    def __init__(self):
        line = self.in_f.readline()

        while (line):
            command = line.split()

            if command[0] == "get":
                self.get(command[1])
            elif command[0] == "prev":
                self.prev(command[1])
            elif command[0] == "next":
                self.next(command[1])
            elif command[0] == "put":
                self.put(command[1], command[2])
            elif command[0] == "delete":
                self.delete(command[1])

            line = self.in_f.readline()


    def get(self, key):
        return self.dictionary.get(key)

    def prev(self, key):
        index_counter = 0
        if self.dictionary[0][0] == key:
            self.out_f.write("None")
            self.out_f.write("\n")
            return None
        for elem in self.dictionary:
            if elem[0] == key:
                break
            else:
                index_counter += 1
        self.out_f.write(self.dictionary[index_counter-1][1])
        self.out_f.write("\n")

    def next(self, key):
        if self.dictionary[-1][0] == key:
            self.out_f.write("None")
            self.out_f.write("\n")
            return None

        index_counter = 0
        for elem in self.dictionary:
            if elem[0] == key:
                break
            else:
                index_counter += 1

        self.out_f.write(self.dictionary[index_counter+1][1])
        self.out_f.write("\n")

    def put(self, key, value):
        self.dictionary.append([key, value])

    def delete(self, key):
        index_counter = 0

        for elem in self.dictionary:
            if elem[0] == key:
                break
            else:
                index_counter += 1

        if index_counter < len(self.dictionary):
            self.dictionary.pop(index_counter)

d = Dictionary()