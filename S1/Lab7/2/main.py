class PhoneBook:
    in_f = open("input", "r")
    out_f = open("output", "w")

    def __init__(self):
        self.book = [ [] for i in range(10)]

        line = self.in_f.readline()

        while (line):
            command = line.split()

            if command[0] == "add":
                self.add_number(command[1], command[2])
            elif command[0] == "del":
                self.del_number(command[1])
            elif command[0] == "find":
                self.find(command[1])

            line = self.in_f.readline()

        print(self.book)
        self.in_f.close()
        self.out_f.close()

    def add_number(self, number, name):
        ind_of_ins = self.hash_func(int(number))

        if type(self.book[ind_of_ins]) != int:
            #Процедура перезаписи
            for elem in self.book[ind_of_ins]:
                if elem[0] == number:
                    elem[1] = name
                    return None
            # Если нет повторов, то делаем такое говно( просто добавляем )
            self.book[ind_of_ins].append([number, name])
        else:
            self.book[ind_of_ins] = [number, name]


    def del_number(self, number):
        ind_of_del = self.hash_func(int(number))
        pos_co = 0

        for elem in self.book[ind_of_del]:
            if elem[0] == number:
                print(self.book[ind_of_del].pop(pos_co))
                break
            pos_co += 1


    def find(self, number):
        ind_of_s = self.hash_func(int(number))

        for elem in self.book[ind_of_s]:
            if elem[0] == number:
                self.out_f.write(elem[1])
                self.out_f.write("\n")
                return None
        self.out_f.write("not found")
        self.out_f.write("\n")


    def hash_func(self, value):
        return value % 10

p = PhoneBook()
