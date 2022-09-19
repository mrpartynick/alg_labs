# Класс, который представляет собой узел в дереве.
class BinarySearchNode:
    # Каждый узел имеет значение, левого и правого ребенка.
    value = None
    left_children = None
    right_children = None

    def __init__(self, value=None):
        self.value = value


# Класс, который представляет само дерево.
class BinarySearchTree:
    root = BinarySearchNode()
    values = []

    # Инициализатор, который принимает название файла с коммандами и считывает их.
    def __init__(self, input_file):
        input_file = open(input_file, "r")

        for command in input_file.readlines():
            self.command_handler(command)

        input_file.close()

    # Функция добавления элемента в дерево.
    def add_new_value(self, adding_value):
        if adding_value in self.values:
            return None
        else:
            self.values.append(adding_value)
        # Если корневого элемента нет, то устанавливаем добавляемое значение в качестве корневого.
        if self.root.value is None:
            self.root.value = adding_value
        # Если корневой элемент есть.
        else:
            current_node = self.root

            # Инициализируем добавляемое значение, как узел.
            adding_node = BinarySearchNode(adding_value)

            # Пока мы не дошли до бездетного узла.
            while (current_node):
                # Если добавляемое значение больше значения в рассматриваемом узле.
                if adding_value > current_node.value:
                    # Если у рассматриваемого узла нет правого ребенка.
                    if current_node.right_children is None:
                        # Правым ребенком будет наш добавляемый узел.
                        current_node.right_children = adding_node
                        break
                    else:
                        # Иначе рассматриваемым узлом становится правый ребенок того, кого мы смотрели до этого.
                        current_node = current_node.right_children
                # Если добавляемый меньше рассматриваемого. ( Прописание полного условия обеспечивает
                # фильтрацию повторов)
                elif adding_value < current_node.value:
                    # Та же процедура, только для левых детей.
                    if current_node.left_children is None:
                        current_node.left_children = adding_node
                        break
                    else:
                        current_node = current_node.left_children

    # Функция нахождения минимального значения, большего даннного.
    def lower_buff(self, value):
        current_node = self.root
        remembered_value = 0

        while (current_node):

            if value >= current_node.value:
                current_node = current_node.right_children
            elif value < current_node.value:
                remembered_value = current_node.value
                current_node = current_node.left_children
            else:
                break

        return remembered_value

    # Функция обработки комманд из текстового файла.
    def command_handler(self, str_command):
        data = int(str_command[1:])
        if str_command[0] == "+":
            self.add_new_value(data)
        else:
            print(self.lower_buff(data))


tree = BinarySearchTree("input_data")
