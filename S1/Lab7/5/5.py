class SomebodyWannaSomeDemocracy:
    in_f = open("input", "r")
    out_f = open("output", "w")

    results = [[] for i in range(100)]
    not_empty_cells = []

    def __init__(self):
        line = self.in_f.readline()

        while (line):
            data = line.split()

            self.add_data(data[0], data[1])

            line = self.in_f.readline()
        for index in self.not_empty_cells:
            for elem in self.results[index]:
                self.out_f.write(elem[0] + " " + elem[1])
                self.out_f.write("\n")



    def add_data(self, name, value):
        ind_of_data = self.hash_func(name)
        if ind_of_data not in self.not_empty_cells:
            self.not_empty_cells.append(ind_of_data)
        if self.results[ind_of_data] == []:
            self.results[ind_of_data].append([name, value])
        else:
            for elem in self.results[ind_of_data]:
                if elem[0] == name:
                    votes = elem[1]
                    elem[1] = str(int(votes) + int(value))

    def hash_func(self, name):
        hash_sum = 0

        for elem in name:
            hash_sum += ord(elem)

        return hash_sum % 100

d = SomebodyWannaSomeDemocracy()