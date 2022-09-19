# Класс, который представляет собой узел в дереве.
class BinarySearchNode:
    # Каждый узел имеет значение, левого и правого ребенка.
    value = None
    left_children = None
    right_children = None
    parent = None

    def __init__(self, value=None):
        self.value = value


# Класс, который представляет само дерево.
class BinarySearchTree:
    root = BinarySearchNode()
    tree = []
    tree_array = []

    # Инициализатор, который принимает название файла с данными, строит по ним дерево и проверяет его.
    def __init__(self, input_data):

        # Создаем массив с данными из файла
        tree_array = self.make_tree_array(input_data)

        self.tree_array = tree_array
        # Строим дерево по данным из массива.
        self.make_binary_search_tree()

        # Проверяем дерево на корректность.
        #print(self.tree_identification())

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

    # Функция, которая считывает данные из файла и организует их в массив.
    def make_tree_array(self, input_data):
        input_data = open(input_data, "r")

        first_line_flag = 0
        tree = []

        # Построчно считываем файл.
        for line in input_data.readlines():
            # Если строчка первая - пропускаем её.
            if first_line_flag == 0:
                first_line_flag += 1
                continue
            else:
                # Удаляем всякий мусор из строки и преобразуем её в массив с числами.
                line = line.split(sep=" ")
                line[-1] = line[-1].replace("\n", "")
                node = list(map(int, line))

                # Добавляем узел в общий массив,
                tree.append(node)

        # Заменяем значения в массиве с данными из файла на BinarySearchNode с соот. значениями.
        for node in tree:
            node[0] = BinarySearchNode(node[0])

        return tree

    # Функция, которая по данным из массива строит дерево.
    def make_binary_search_tree(self):
        output_file = open("output.txt", "w")

        # Проходимся по каждому узлу из массива и устанавливаем для него левого и правого ребенка.
        for node in self.tree_array:
            # Считываем данные из узла в массиве.
            node_value = node[0].value
            node_left_child_index = node[1] - 1
            node_right_child_index = node[2] - 1

            # Если корневой элемент ещё не установлен.
            if self.root.value is None:
                self.root.value = node_value

                if node_left_child_index != -1:
                    self.root.left_children = self.tree_array[node_left_child_index][0]
                    self.tree_array[node_left_child_index][0].parent = self.root
                if node_right_child_index != -1:
                    self.root.right_children = self.tree_array[node_right_child_index][0]
                    self.tree_array[node_right_child_index][0].parent = self.root

            # Иначе.
            else:
                tree_node = node[0]

                if node_left_child_index != -1:
                    tree_node.left_children = self.tree_array[node_left_child_index][0]
                    self.tree_array[node_left_child_index][0].parent = tree_node

                if node_right_child_index != -1:
                    tree_node.right_children = self.tree_array[node_right_child_index][0]
                    self.tree_array[node_right_child_index][0].parent = tree_node


                if self.is_value_in_tree(node_value):
                    pass
                else:
                    output_file.write("NO")
                    return None

        output_file.write("YES")


    # Функция, которая проверяет, является ли наше дерево правильно построенным.
    def tree_identification(self):
        output_file = open("output.txt", "w")

        # Проходимся по каждому значению узла в массиве и проверяем, есть ли он в дереве. Если нет - то дерево некор.
        for elem in self.tree_array:
            result = self.is_value_in_tree(elem[0].value)

            if result is False:
                output_file.write("NO")
                return None

        output_file.write("YES")


tree = BinarySearchTree("input.txt.txt")
