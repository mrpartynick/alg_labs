input_data = open("input_data", "r")

c = 0
for line in input_data.readlines():
    if c == 0:
        n = int(line)
        tree = []
    else:
        line = line.split(sep=" ")
        line[-1] = line[-1].replace("\n", "")
        line = list(map(int, line))

        value = line[0]
        left_child = line[1]
        right_child = line[2]

        node = [value, left_child, right_child]

        tree.append(node)
    c += 1

for node in tree:
    value = node[0]
    left_child = node[1]
    right_child = node[2]

    while left_child != -1:
        left_child_value = tree[left_child][0]
        if left_child_value < value:
            value = tree[left_child][0]
            left_child = tree[left_child][1]
        else:
            print("Incorrect")
            break

    while right_child != -1:
        right_child_value = tree[right_child][0]
        if right_child_value > value:
            value = tree[right_child][0]
            right_child = tree[right_child][1]
        else:
            print("Incorrect")
            break








root = tree[0]

root_value = root[0]
left_child_index = root[1]
right_child_index = root[2]

for node in tree:
    value = node[0]
    left_child_index = node[1]
    right_child_index = node[2]
    result = "Correct"

    while left_child_index != -1:
        left_child_value = tree[left_child_index][0]
        if left_child_value < value:
            print(left_child_value, "is less then", value)
            value = left_child_value
            left_child_index = tree[left_child_index][1]
        else:
            result = "Incorrect"
            break

    value = node[0]
    left_child_index = node[1]
    right_child_index = node[2]

    while right_child_index != -1:
        right_child_value = tree[right_child_index][0]
        if right_child_value > value:
            print(right_child_value, "is greater then", value)
            value = right_child_value
            right_child_index = tree[right_child_index][2]
        else:
            result = "Incorrect"
            break

    print(result)

node_value = node[0]
node_left_child_index = node[1]
node_right_child_index = node[2]

if node_left_child_index != -1:
    self.root.left_children = BinarySearchNode(tree_array[node_right_child_index])
else:
    self.root.right_children = BinarySearchNode(tree_array[node_right_child_index])