# Первый максимум - самый правый элемент. Второй максимум - либо левый ребенок самого правого, либо его родитель.

# Класс, который представляет собой узел в дереве.
class BinaryMaximumNode:
    # Каждый узел имеет значение, левого и правого ребенка.
    value = None
    left_children = None
    right_children = None

    parent = None

    def __init__(self, value=None):
        self.value = value


class BinaryMaximumTree:
    root = None
    # Переменная, которая указывает, каким по счету максимумом является наш корень.
    root_maximum = 1

    # Переменные, которые показывают длину правой и левой веток.
    length_of_left_branch = 0
    length_of_right_branch = 0

    def __init__(self):
        input_file = open("input_data", "r")

        # Считываем команды из файла и обрабатываем их.
        for command in input_file.readlines():
            self.command_handler(command)

        input_file.close()

    # Функция добавления элемента.
    def add_value(self, value):
        # Инициализируем добавляемый узел.
        adding_node = BinaryMaximumNode(value)

        # Если корня нет, то добавляемое значение - корень.
        if self.root is None:
            self.root = adding_node
        else:
            current_node = self.root

            # Если добавляемое значение больше корня, то вставляем значение в правую ветку.
            if value > current_node.value:
                self.root_maximum += 1
                self.length_of_right_branch += 1

                while True:
                    if current_node.right_children is None:
                        current_node.right_children = adding_node
                        break
                    else:
                        next_node = current_node.right_children

                        if value < next_node.value:
                            current_node.right_children = adding_node
                            adding_node.right_children = next_node
                            break
                        else:
                            current_node = next_node
            else:
                # Иначе - добавляем в левую ветку.
                self.length_of_left_branch += 1

                while True:
                    if current_node.left_children is None:
                        current_node.left_children = adding_node
                        break
                    else:
                        next_node = current_node.left_children

                        if value > next_node.value:
                            current_node.left_children = adding_node
                            adding_node.left_children = next_node
                            break
                        else:
                            current_node = next_node

        # Проводим балансировку.
        self.balance()

    # Функция балансировки.
    def balance(self):
        # Находим разницу между длинами веток.
        dif = abs(self.length_of_left_branch - self.length_of_right_branch)

        # Если длина > 2, то метро Люблино, работаем.
        if dif > 2:
            # Левая ветка длинее - двигаем влево.
            if self.length_of_left_branch > self.length_of_right_branch:
                for i in range(dif):
                    self.root = self.root.left_children
                    self.length_of_left_branch -= 1
            else:
                # Правая ветка длинее - двигаем вправо.
                for i in range(dif):
                    self.root = self.root.right_children
                    self.length_of_right_branch -= 1
                    self.root_maximum -= 1

    def delete_value(self, value):
        # Если нам нужно удалить корень.
        if value == self.root.value:

            # Если у корня есть только левый ребенок.
            if self.root.right_children is None and self.root.left_children is not None:
                self.root = self.root.left_children
                self.root_maximum -= 1

            # Если у корня есть только правый ребенок.
            elif self.root.left_children is None and self.root.right_shildren is not None:
                self.root = self.root.right_children
                self.root_maximum -= 1

            # Если у корня нет детей.
            elif self.root.left_children is None and self.root.right_children is None:
                self.root = None
                self.root_maximum = 1

            # Если у корня есть оба ребенка.
            elif self.root.right_children is not None and self.root.left_children is not None:
                new_root = self.root.right_children
                new_root.left_children = self.root.left_children
                self.root_maximum -= 1

                self.root = new_root

        elif value > self.root.value:
            current_node = self.root

            while True:
                next_node = current_node.right_children

                if next_node.value == value:
                    break
                else:
                    current_node = next_node

            current_node.right_children = next_node.right_children

        elif value < self.root.value:
            current_node = self.root

            while True:
                next_node = current_node.left_children

                if next_node.value == value:
                    break
                else:
                    current_node = next_node

            current_node.left_children = next_node.left_children

    def print_maximum(self, number):
        current_node = self.root

        if number < self.root_maximum:
            for i in range(number):
                current_node = current_node.right_children

            print(current_node.value)

        elif number == self.root_maximum:
            print(self.root.value)

        elif number > self.root_maximum:
            for i in range(number - self.root_maximum):
                current_node = current_node.left_children

            print(current_node.value)

    def command_handler(self, str_command):
        if str_command[0] == "+":
            data = int(str_command[3:])
            self.add_value(data)
        elif str_command[0] == "-":
            data = int(str_command[3:])
            self.delete_value(data)
        elif str_command[0] == "0":
            data = int(str_command[2:])
            self.print_maximum(data)


tree = BinaryMaximumTree()
