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
        # Костыль, который позволет не добавлять дубликаты.
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

        if remembered_value != 0:
            print(remembered_value)

    # Функция, которая находит элемент, максимальный строго меньший данного.
    def upper_buff(self, value):
        current_node = self.root
        remembered_value = 0

        while (current_node):
            if value <= current_node.value:
                current_node = current_node.left_children
            else:
                remembered_value = current_node.value
                current_node = current_node.right_children
        if remembered_value != 0:
            print(remembered_value)

    # Функция, которая проверяет существование значения в дереве.
    def is_value_in_tree(self, value):
        current_node = self.root

        while (current_node):
            if value == current_node.value:
                return True
            elif value > current_node.value:
                current_node = current_node.right_children
            elif value < current_node.value:
                current_node = current_node.left_children

        return False

    # Костыльная кринжофункция удаления элемента из дерева.
    def delete_value(self, value):

        if self.is_value_in_tree(value):
            node_for_deletion = BinarySearchNode()
            current_node = self.root
            father_node = None

            c = 0
            while (current_node):
                if value == current_node.value:
                    node_for_deletion = current_node
                    break
                elif value > current_node.value:
                    father_node = current_node
                    current_node = current_node.right_children
                elif value < current_node.value:
                    father_node = current_node
                    current_node = current_node.left_children

            if node_for_deletion.left_children is None and node_for_deletion.right_children is None:
                if father_node.right_children is not None and father_node.right_children.value == value:
                    father_node.right_children = None
                elif father_node.left_children is not None and father_node.left_children.value == value:
                    father_node.left_children = None
            elif (node_for_deletion.left_children is None and node_for_deletion.right_children is not None) or \
                    (node_for_deletion.right_children is None and node_for_deletion.left_children is not None):
                if node_for_deletion.right_children is None:
                    node_for_deletion.value = node_for_deletion.left_children.value
                    node_for_deletion.left_children = None
                else:
                    node_for_deletion.value = node_for_deletion.right_children.value
                    node_for_deletion.right_children = None
            elif node_for_deletion.right_children is not None and node_for_deletion.left_children is not None:
                end_left_child = node_for_deletion.right_children

                while (end_left_child):
                    end_left_child = end_left_child.left_children

                node_for_deletion.value = end_left_child.value

                if end_left_child.right_children is not None:
                    end_left_child.value = end_left_child.right_children.value
                    end_left_child.right_children = None

        # Функция обработки комманд из текстового файла.

    # Функция обработки текстовых комманд.
    def command_handler(self, str_command):
        if "insert" in str_command:
            self.add_new_value(int(str_command[7:]))
        elif "exists" in str_command:
            print(self.is_value_in_tree(int(str_command[7:])))
        elif "next" in str_command:
            self.lower_buff(int(str_command[5:]))
        elif "prev" in str_command:
            self.upper_buff(int(str_command[5:]))
        elif "delete" in str_command:
            print(self.delete_value(int(str_command[7:])))


tree = BinarySearchTree("input_data")
